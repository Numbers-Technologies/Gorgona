import ast
import os
import queue
import sys
import threading
import time

import sounddevice as sd
import torch
import vosk
from PyQt5 import QtCore, QtWidgets, QtGui
from google.cloud import dialogflow_v2beta1 as dialogflow

import config  # Local module. config.py
from Functions import Weather, Clock

#  Global variables.
LANGUAGE: str = 'ru'
app: object  # PyQt5 Application: gorgona icon.

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'gorgona_key.json'  # DialogFlow Service key.
DIALOGFLOW_PROJECT_ID: str = 'gorgona-350503'  # Google Cloud project.
DIALOGFLOW_LANGUAGE_CODE: str = LANGUAGE  # DialogFlow Language.
SESSION_ID: str = 'me'  # Session name.


def show_icon_gorgona() -> None:
    """ Gorgona icon. We use pyqt5 for display image. """
    global app
    app = QtWidgets.QApplication(sys.argv)
    screen = QtWidgets.QDesktopWidget().screenGeometry()  # Get screen width and height.
    window = QtWidgets.QWidget()
    window.setWindowFlags(QtCore.Qt.Window |
                          QtCore.Qt.FramelessWindowHint |
                          QtCore.Qt.WindowStaysOnTopHint)

    # -------------------- 1920//2 - 170//2 = 960 - 85 = 875. Create a window in the center of the primary monitor.
    window.setGeometry(screen.width() // 2 - 400 // 2, screen.height() // 2 + 200, 400, 400)

    # -------------------------------------------- x -- y resolution.
    pixmap = QtGui.QPixmap("gorgona.png").scaled(400, 400,
                                                 QtCore.Qt.KeepAspectRatio,
                                                 QtCore.Qt.FastTransformation)
    pal = window.palette()
    pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
    pal.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
    window.setPalette(pal)
    window.setMask(pixmap.mask())
    window.show()
    app.exec()  # Application loop.


class Recognition:
    def __init__(self) -> None:
        """Initialize voice recognition class."""
        self.model = vosk.Model("model_small")  # Model. You can use Big (2.5G) or small (1G)
        self.samplerate = 16000
        self.device = 1
        self.running = False
        self.q = queue.Queue()
        self.session_client = dialogflow.SessionsClient()  # Initialize DialogFlow client.
        self.session = self.session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    def _show_icon(self):
        self.gorg_ic = threading.Thread(target=show_icon_gorgona)
        self.gorg_ic.start()

    def _destroy_icon(self):
        self.running = False
        app.quit()

    def q_callback(self, indata, status, *args) -> None:
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def _recognize(self, text) -> None:
        if text.startswith(config.VA_NAME):  # обращение к горгоне
            if self.running is False:  # If PyQt5 application not running {
                self.running = True  # running = True => create PyQt5 Application. }
                self._show_icon()
            text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
            query_input = dialogflow.types.QueryInput(text=text_input)

            try:
                response = self.session_client.detect_intent(session=self.session, query_input=query_input)
                text = response.query_result.fulfillment_text  # Dialogflow response
                intent = response.query_result.intent.display_name  # Dialogflow intent

                if intent == "smalltalk.greetings.bye":  # Quit from gorgona and destroy pyqt5 app.
                    self._destroy_icon()
                    gorgona.say_something(text)

                elif intent == "smalltalk.weather":
                    gorgona.say_something("Сейчас посмотрю..")
                    weather = Weather.Weather().get_weather(city=text)  # <------ FIX ME.
                    gorgona.say_something(weather)

                elif intent == "smalltalk.system.time":
                    gorgona.say_something(Clock.Clocks.time(city=text))

                else:
                    gorgona.say_something(text)

            except Exception as ex:
                print("No", ex)

            print(response.query_result)

    def listen(self):
        """ Get voice from microphone. """
        with sd.RawInputStream(samplerate=self.samplerate,
                               blocksize=8000,
                               device=self.device,
                               dtype='int16',
                               channels=1,
                               callback=self.q_callback):
            record = vosk.KaldiRecognizer(self.model, self.samplerate)

            while True:
                data = self.q.get()
                if record.AcceptWaveform(data):
                    g = record.Result()
                else:
                    g = record.PartialResult()

                # You can use this code, but this method slow:
                # if record.AcceptWaveform(data)
                #    g = record.Result()

                g = ast.literal_eval(g)  # string to dict with ast module.
                try:
                    print(g['text'])  # Get text from dict.
                    self._recognize(g['text'])  # Send it to DialogFlow and recognize.
                except Exception:
                    print("part")
                    pass


class Gorgona:
    def __init__(self) -> None:
        """ Initialize Gorgona voice. """
        language: str = LANGUAGE
        model_id: str = 'ru_v3'
        self.sample_rate: int = 48000
        self.speaker: str = 'baya'
        self.put_accent: bool = True
        self.put_yo: bool = True
        device: object = torch.device(
            'cpu')  # cuda, xpu, mkldnn, opengl, opencl, ideep, hip, ve, ort, mlc, vulkan, hpu etc...

        self.model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                       model='silero_tts',
                                       language=language,
                                       speaker=model_id)
        self.model.to(device)

    def say_something(self, text: str) -> None:
        audio = self.model.apply_tts(text=text,
                                     speaker=self.speaker,
                                     sample_rate=self.sample_rate,
                                     put_accent=self.put_accent,
                                     put_yo=self.put_yo)
        sd.play(audio, self.sample_rate)
        time.sleep(len(audio) / self.sample_rate)
        sd.stop()


gorgona = Gorgona()
#root = Recognition()
#root.listen()


time = Clock.Clocks.clock_alarm("шестнадцать сорок три")
gorgona.say_something(time)

# Будильник
# Время
# Таймер
# Секундомер
#

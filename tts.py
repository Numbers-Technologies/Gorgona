import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('voice', self.engine.getProperty('voices')[2].id)
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
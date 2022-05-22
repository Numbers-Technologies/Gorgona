from transliterate import translit
from pyowm import OWM
from config import OWM_TOKEN
from num2words import num2words

class Weather:
    global owm, mgr
    mgr = OWM(OWM_TOKEN).weather_manager()

    @staticmethod
    def get_weather(city: str) -> str:
        observation = mgr.weather_at_place(translit(city, reversed=True))
        w = observation.weather
        weather = int(w.temperature('celsius')['temp'])
        weather = num2words(weather, lang="ru")
        del observation, w
        return weather + " градусов"



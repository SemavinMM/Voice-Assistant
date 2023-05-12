from pyowm import OWM
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from gtts import gTTS
from playsound import playsound


config_dict = get_default_config()
config_dict['language'] = 'ru'
country = input("Введите свою страну ")
place = input("Введите свой город ")
country_and_place = place + ", " + country

owm = OWM('232f2a241eee13d7d29f4370a4eb6513')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(country_and_place)
w = observation.weather

status = w.detailed_status
w.wind()
humidity = w.humidity
temp = w.temperature('celsius')['temp']

#weather
def say_weather():
    text_val = f'В городе {str(place)} сейчас {str(status)}.Температура{str(round(temp))}градусов по цельсию. Влажность составляет {str(humidity)} процентов'
    language = 'ru'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save('testW.mp3')
    playsound('testW.mp3')

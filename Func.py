from gtts import gTTS
from playsound import playsound
from datetime import date
import time


#hello
name1 = str(input("Введите своё имя "))
def say_hello():
    text_val = f'Привет{name1}'
    language = 'ru'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save('test.mp3')
    playsound('test.mp3')

#time
def say_time(num):
    question = time.strftime('%H:%M')
    text_val = f'Сейчас {question}'
    language = 'ru'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save('testT'+str(num)+'.mp3')
    playsound('testT'+str(num)+'.mp3')


#goodbye
def say_bye():
    text_val = f'Пока {name1}'
    language = 'ru'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save('testB.mp3')
    playsound('testB.mp3')

#date
def say_date():
    question = date.today()
    text_val = f'Сегодня {question}'
    language = 'ru'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save('testD'+str()+'.mp3')
    playsound('testD'+str()+'.mp3')
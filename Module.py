from Func import *
from Weather_func import *

say_hello()


i = 0
question = str(input())
while question.upper() != 'ПОКА':
    i += 1
    question = question.upper()
    if question == 'ВРЕМЯ':
        say_time(i)
    if question == 'ДАТА':
        say_date()
    if question == 'ПОГОДА':
        say_weather()
    question = str(input())
say_bye()
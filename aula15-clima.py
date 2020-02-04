import requests
import json
import datetime

cidade = input("Escreva sua cidade: ")

req = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=29a246b1b59f2718d4e4c81c23a8e5a9')
tempo = json.loads(req.text)

print('\n ---- Clima em tempo real ----\n')
print('Condição climática: ', tempo['weather'] [0] ['main'])
print('Temperatura: ', "%.2f" % float(tempo['main'] ['temp'] - 273.15))
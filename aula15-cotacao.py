import requests
import json
import datetime
import time

titulo = 'API Cotação das MOEDAS'
print(titulo.center(25, "-") + "\n")

while True:

    print("COTAÇÃO EM TEMPO REAL\nData e hora da consulta: ", str(datetime.datetime.now()) + "\n")
    req = requests.get('https://economia.awesomeapi.com.br/all')
    dici = json.loads(req.text)

    print(' - Valor DÓLAR atualizado:', dici['USD'] ['high'] + "\n - Menor valor do DÓLAR hoje:", dici['USD'] ['low'] + "\n")
    print(' - Valor BITCOIN atualizado:', dici['BTC'] ['high'] + "\n - Menor valor do BITCOIN hoje:", dici['BTC'] ['low'] + "\n")

    time.sleep(5)

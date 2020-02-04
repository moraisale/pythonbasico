import re
import requests

req = requests.get('https://zecoxinha.com.br/contato/')

padrao = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", req.text) # RAW string

try:
    print(padrao[1])
except:
    print("Padrao nao encontrado")
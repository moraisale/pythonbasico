import requests

cabecalho = {'User-agent': 'Windows 11'}
dados = {'username' : 'alex11', 'senha' : 'leleco123'}

try:
    requisicao = requests.post("https://putsreq.com/os60NekRkbmwbZnnSdrY", headers = cabecalho, data = dados)
    print(requisicao.text)
    print("Requisicao concluida.\nCodigo: ", requisicao.status_code)
except Exception as erro:
    print("Endereco nao encontrado\nErro: ", erro)
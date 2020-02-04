import time

def abre_arquivo():
    try:
        arquivo = open('arquivo.txt')
        return True
    except Exception as erro:
        print("Nao foi possivel abrir o arquivo", erro)
        return False

while not abre_arquivo():
    print("Tentando abrir arquivo")
    time.sleep(3)

print("Arquivo aberto com sucesso")
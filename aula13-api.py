import requests
import json

tt = "API FILMES"
print(tt.center(20, "*"))

def requisicao(titulo): # cria um parametro para ser recebido
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=73f10b10')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Filme nao encontrado')
        return None
def printar_detalhes(filme):
    print('Titulo: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Diretor: ', filme['Director'])
    print('Nota: ', filme['imdbRating'])


sair = False
while not sair:
    op = input("Escreva o nome de um filme ou digite SAIR para encerrar o programa: ") # op sera o parametro 'titulo' da funcao 'requisicao'

    if op == 'SAIR':
        print('Programa finalizado')
        sair = True
    else:
        filme = requisicao(op) # A variavel 'filme' recebe a funcao 'requisicao' com o parametro 'op' que substitui 'titulo'
        if filme['Response'] == 'False':
            print("Filme nao encontrado")
        else:
            printar_detalhes(filme)

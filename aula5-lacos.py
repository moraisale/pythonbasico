t0 = "Convidados da festa"

print(t0.center(50, "*"))

num_convidados = input("Quantas pessoas serao convidadas para a festa: ")
lista_convidados = []
i = 0

while i < int(num_convidados):
    nome_convidado = input('Nome do convidado ' + str(i) + ': ')
    i += 1
    lista_convidados.append(nome_convidado)

print(lista_convidados)
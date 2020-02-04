arquivo = open('arquivo.txt', 'r+')

for i in range(0, 10):
    arquivo.write("alexandre \n")

print(arquivo.read())

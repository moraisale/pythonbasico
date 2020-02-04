t0  = 'Questionário'
print(t0.center(50, "*"))

altura_p = 1.60
idade_p = 18

altura = input('qual sua altura:\n')
idade = input('qual sua idade:\n')


if altura > '1.60' and idade > '18':
    print('Voce esta apto para o exercito')
else:
    print('voce n esta apto para o exercito')
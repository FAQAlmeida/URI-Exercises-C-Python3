lista = list()
while True:
    a = int(input())
    if a == 2002:
        lista.append('Acesso Permitido')
        break
    else:
        lista.append('Senha Invalida')
for x in lista:
    print(x)
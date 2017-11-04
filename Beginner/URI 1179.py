lista = list()
lista2 = list()

for x in range(15):
    n = int(input())
    if n % 2 == 0:
        lista.append('par[{0}] = {1}'.format(len(lista),n))
        if len(lista) == 5:
            for y in lista:
                print(y)
            lista.clear()
    elif n % 2 == 1:
        lista2.append('impar[{0}] = {1}'.format(len(lista2),n))
        if len(lista2) == 5:
            for y in lista2:
                print(y)
            lista2.clear()
for x in lista2:
    print(x)
for x in lista:
    print(x)
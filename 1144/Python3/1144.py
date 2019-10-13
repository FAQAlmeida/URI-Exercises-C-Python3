n = int(input())
lista = list()
for x in range(1, n + 1):
    lista.append('{} {} {}'.format(x,pow(x,2), pow(x,3)))
    lista.append('{} {} {}'.format(x, pow(x, 2) + 1, pow(x, 3) + 1))
for x in lista:
    print(x)
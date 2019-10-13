lista = list()

n = float(input())

for x in range(100):
    lista.append(n)
    n /= 2

for x in range(len(lista)):
    print('N[{}] = {:.4f}'.format(x,lista[x]))
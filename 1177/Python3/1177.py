lista = list()

n = int(input())
a = 0
for x in range(1000):
    lista.append(a)
    a += 1
    if a == n :
        a = 0

for x in range(len(lista)):
    print('N[{}] = {}'.format(x,lista[x]))
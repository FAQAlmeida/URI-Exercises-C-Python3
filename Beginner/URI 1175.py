lista = list()
n1 = 0
n2 = 1
lista.append(n1)
lista.append(n2)
for x in range(64):
    lista.append(n1 + n2)
    aux = n1
    n1 = n2
    n2 += aux

a = int(input())

for x in range(a):
    b = int(input())
    print('Fib({}) = {}'.format(b, lista[b]))
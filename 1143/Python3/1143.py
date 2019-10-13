n = int(input())
lista =list()
for x in range(1,1+n):
    lista.append('{} {} {}'.format(x, pow(x,2), pow(x,3)))
for x in lista:
    print(x)
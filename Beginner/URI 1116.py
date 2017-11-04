N = int(input())
lista = list()
for x in range(N):
    a, b = map(float,input().split())
    if b == 0:
        lista.append('divisao impossivel')
    else:
        lista.append(a/b)
for x in lista:
    print(x)
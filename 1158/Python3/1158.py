n= int(input())

lista = list()

for a in range(n):
    soma = 0
    count = 0
    x, y = map(int,input().split())
    while True:
        if x % 2 != 0:
            soma += x
            count += 1
        x += 1
        if count == y:
            break
    lista.append(soma)
for a in lista:
    print(a)
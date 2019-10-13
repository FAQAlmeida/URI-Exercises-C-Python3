n = int(input())

lista = list(map(int,input().split()))

for x in range(n):
    if x == 0:
        menor = lista[x]
        posicao = x
    if lista[x] < menor:
        menor = lista[x]
        posicao = x
print('Menor valor: {}\nPosicao: {}'.format(menor, posicao))
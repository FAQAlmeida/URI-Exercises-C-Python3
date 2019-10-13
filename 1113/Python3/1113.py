lista = list()
while True:
    a, b = map(int,input().split())
    if a == b:
        break
    if a > b:
        lista.append('Decrescente')
    else:
        lista.append('Crescente')
for x in lista:
    print(x)
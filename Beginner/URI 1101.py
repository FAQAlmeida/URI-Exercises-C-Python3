listaT = list()
listaS = list()
while True:
    lista = list()
    soma = 0
    a, b = map(int,input().split())
    if a <= 0 or b <= 0:
        break
    elif(a <= b):
        for x in range(a, b + 1):
            lista.append(x)
            soma += x
            resp = ' '.join(map(str,lista))
    else:
        for x in range(b, a + 1):
            lista.append(x)
            soma += x
            resp = ' '.join(map(str,lista))
    if len(lista) != 0:
        listaT.append(resp)
        listaS.append(soma)
for x in range(len(listaT)):
    print(listaT[x], 'Sum={}'.format(listaS[x]))



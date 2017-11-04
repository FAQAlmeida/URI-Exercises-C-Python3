n = int(input())
listaM = list()
for x in range(n):
    a  = int(input())
    lista = list()
    for y in range(1, a):
        if a % y == 0:
            lista.append(y)
    if sum(lista) == a:
        listaM.append('{} eh perfeito'.format(a))
    else:
        listaM.append('{} nao eh perfeito'.format(a))
for x in listaM:
    print(x)
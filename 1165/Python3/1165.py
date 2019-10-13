n = int(input())
listaM = list()
for x in range(n):
    a = int(input())
    if a == 0:
        b = False
    elif a == 1 or a == 2:
        b = True
    for v in range(2,a):
        if a % v == 0:
            b = False
            break
        else:
            b = True
    if b == True:
        listaM.append('{} eh primo'.format(a))
    else:
        listaM.append('{} nao eh primo'.format(a))
for x in listaM:
    print(x)
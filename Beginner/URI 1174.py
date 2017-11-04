lista = list()
for x in range(100):
    lista.append(float(input()))
for x in range(len(lista)):
    if lista[x] <= 10:
        print('A[{}] = {:.2}'.format(x,lista[x]))
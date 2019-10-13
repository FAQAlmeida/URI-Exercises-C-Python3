lista = list()
while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        lista.append(idade)

media = sum(lista) / len(lista)

print('{:.2f}'.format(media))
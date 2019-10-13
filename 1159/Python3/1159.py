lista = list()
while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    count = 0
    while True:
        if n % 2 == 0:
            count += 1
            soma += n
        n += 1
        if count == 5:
            break
    lista.append(soma)
for x in lista:
    print(x)
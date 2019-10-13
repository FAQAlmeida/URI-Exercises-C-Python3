N = int(input())
lista = list()
for x in range(N):
    soma = 0
    a, b = input().split()
    a, b = [int(a),int(b)]
    if a <= b:
        for y in range(a + 1,b):
            if y % 2 != 0:
                soma += y
    else:
        for y in range(b + 1,a):
            if y % 2 != 0:
                soma += y
    lista.append(soma)
for resul in lista:
    print(resul)
posi = 0
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista = [a,b,c,d,e,f]


for x in range(len(lista)):
    if(lista[x] > 0):
        posi += 1
lista1 = list()
for x in range(len(lista)):
    if(lista[x] > 0):
        lista1.append(lista[x])
media = sum(lista1)/len(lista1)

print("{0} valores positivos\n{1:.1f}".format(posi,media))
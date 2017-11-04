lista = list()
while True:
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        lista.append('primeiro')
    elif x < 0 and y > 0:
        lista.append('segundo')
    elif x < 0 and y < 0:
        lista.append('terceiro')
    elif x > 0 and y < 0:
        lista.append('quarto')
    else:
        break
for x in lista:
    print(x)
resp = True
while resp == True:
    lista = list()
    nota1 = float(input())
    nota2 = float(input())
    while True:
        if nota1 < 0 or nota1 > 10:
           nota1 = float(input())
        elif nota2 < 0 or nota2 > 10:
          nota2 = float(input())
        else:
          break
        lista.append('nota invalida')
    media = (nota1 + nota2) / 2
    for x in lista:
        print(x)
    print('media = {0:.2f}'.format(media))

    while True:
        print('novo calculo (1-sim 2-nao)')
        resp = input()
        if resp == '1':
            resp = True
            break
        elif resp == '2':
            resp = False
            break
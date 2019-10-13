class main:
    par= 0
    impar = 0
    posi = 0
    nega = 0
    inp = [0,0,0,0,0]
    for x in range(5):
        inp[x] = int(input())
    for x in range(5):
        if(inp[x] % 2 == 0):
            par += 1
        else:
            impar += 1
        if(inp[x] < 0):
            nega += 1
        elif(inp[x] > 0):
            posi += 1

    print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(par,impar,posi,nega))
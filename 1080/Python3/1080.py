class main:
    for a in range(100):
        inp = int(input())
        if(a == 0):
            maior = inp
            posicao = 1
        elif(inp > maior):
            maior = inp
            posicao = a + 1
    print('{}\n{}'.format(maior,posicao))
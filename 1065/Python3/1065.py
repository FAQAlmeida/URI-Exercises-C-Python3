class main:
    resposta = 0
    for x in range(5):
        inp = float(input())
        if(inp % 2 == 0):
            resposta += 1
    print("{} valores pares".format(resposta))
class main:
    resposta = 0
    for x in range(6):
        inp = float(input())
        if(inp >= 0):
            resposta += 1
    print("{} valores positivos".format(resposta))
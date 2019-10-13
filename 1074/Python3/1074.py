class main:
    i = int(input())
    for x in range(i):
        inp = float(input())
        if(inp == 0):
            resposta = 'NULL'
        elif(inp % 2 == 0):
            resposta = 'EVEN'
        else:
            resposta = 'ODD'
        if(resposta == 'NULL'):
            print(resposta)
        elif(inp < 0):
            resp = 'NEGATIVE'
            print("{} {}".format(resposta, resp))
        else:
            resp = 'POSITIVE'
            print("{} {}".format(resposta, resp))
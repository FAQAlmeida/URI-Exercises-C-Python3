class main:
    cont = int(input())
    quantC = 0
    quantS = 0
    quantR = 0
    quantT = 0
    for a in range(cont):
        b, tipo = input().split()
        quant = int(b)
        if(tipo == 'C'):
            quantC += quant
        elif(tipo == 'R'):
            quantR += quant
        else:
            quantS += quant
        quantT += quant
    porC = 100*quantC/quantT
    porR = 100*quantR/quantT
    porS = 100*quantS/quantT
    print('Total: {0} cobaias\nTotal de coelhos: {1}\nTotal de ratos: {2}\nTotal de sapos: {3}\nPercentual de coelhos: {4:.2f} %\nPercentual de ratos: {5:.2f} %\nPercentual de sapos: {6:.2f} %'.format(quantT,quantC,quantR,quantS,porC,porR,porS))
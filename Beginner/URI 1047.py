# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
class main:
    hi, mi, hf, mf = input().split()
    hi, mi, hf, mf = [int(hi), int(mi), int(hf), int(mf)]
    if(hi < hf):
        if(mi < mf):
            Hduracao = hf - hi
            Mduracao = mf - mi
        elif(mi > mf):
            Hduracao = hf - hi - 1
            Mduracao = mf - mi + 60
        else:
            Hduracao = hf - hi
            Mduracao = 0
    elif(hi > hf):
        hf += 24
        if(mi < mf):
            Hduracao = hf - hi
            Mduracao = mf - mi
        elif(mi > mf):
            Hduracao = hf - hi
            Mduracao = mf - mi
            Hduracao -= 1
            Mduracao += 60
        else:
            Hduracao = hf - hi
            Mduracao = 0   
    else:
        Hduracao = 24
        if(mi < mf):
            Mduracao = mf - mi
        elif(mi > mf):
            Hduracao -= 1
            Mduracao = (mf + 60) - mi
        else:
            Mduracao = 0
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(Hduracao,Mduracao))
        
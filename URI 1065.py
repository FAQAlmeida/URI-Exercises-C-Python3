# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
class main:
    resposta = 0
    for x in range(5):
        inp = float(input())
        if(inp % 2 == 0):
            resposta += 1
    print("{} valores pares".format(resposta))
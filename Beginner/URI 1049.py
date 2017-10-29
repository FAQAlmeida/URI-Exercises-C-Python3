# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
class main:
    T1 = input().lower()
    T2 = input().lower()
    T3 = input().lower()
    if(T1 == 'vertebrado'):
        if(T2 == 'ave'):
            if(T3 == 'carnivoro'):
                resposta = 'aguia'
            else:
                resposta = 'pomba'
        else:
            if(T3 == 'onivoro'):
                resposta = 'homem'
            else:
                resposta = 'vaca'
    if(T1 == 'invertebrado'):
        if(T2 == 'inseto'):
            if(T3 == 'hematofago'):
                resposta = 'pulga'
            else:
                resposta = 'lagarta'
        else:
            if(T3 == 'hematofago'):
                resposta = 'sanguessuga'
            else:
                resposta = 'minhoca'
    print(resposta)
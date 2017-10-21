# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
class main:
    
    a = int(input())
    for i in range(a+1):
        if(i % 2 == 0 and i != 0):
            print('{}^2 = {}'.format(i, pow(i,2)))
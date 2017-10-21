# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
class main:
    #1º Input
    a = input()
    dia = int(''.join(x for x in a if x.isdigit()))

    #2ºInput
    hora, desc1, minuto, desc2, segundo = input().split()
    hora = int(hora)
    minuto = int(minuto)
    segundo = int(segundo)

    #3ºInput
    b = input()
    diaf = int(''.join(x for x in b if x.isdigit()))

    #4ºInput
    horaf, desc1, minutof, desc2, segundof = input().split()
    horaf = int(horaf)
    minutof = int(minutof)
    segundof = int(segundof)

    #Calculo
    if(dia <= diaf):
        diaFinal = diaf - dia
        if(hora <= horaf):
            horaFinal = horaf - hora
            if(minuto <= minutof):
                minutoFinal = minutof - minuto
                if(segundof >= segundo):
                    segundoFinal = segundof - segundo
                elif(segundof < segundo):
                    segundoFinal = segundof - segundo + 60
                    minutoFinal -= 1
            elif(minuto > minutof):
                minutoFinal = minutof - minuto + 60
                horaFinal -= 1
                if(segundof >= segundo):
                    segundoFinal = segundof - segundo
                elif(segundof < segundo):
                    segundoFinal = segundof - segundo + 60
                    minutoFinal -= 1
        elif(hora > horaf):
            horaFinal = horaf - hora + 24
            diaFinal -= 1
            if(minuto <= minutof):
                minutoFinal = minutof - minuto
                if(segundof >= segundo):
                    segundoFinal = segundof - segundo
                elif(segundof < segundo):
                    segundoFinal = segundof - segundo + 60
                    minutoFinal -= 1
            elif(minuto > minutof):
                minutoFinal = minutof - minuto + 60
                horaFinal -= 1
                if(segundof >= segundo):
                    segundoFinal = segundof - segundo
                elif(segundof < segundo):
                    segundoFinal = segundof - segundo + 60
                    minutoFinal -= 1

    print ('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(diaFinal, horaFinal, minutoFinal, segundoFinal))
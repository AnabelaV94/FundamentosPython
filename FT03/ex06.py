'''Escreve um programa que receba três números reais e indique qual o maior dos três 
números. '''

Numero1 = int(input("Introduza o 1º número\n:"))
Numero2 = int(input("Introduza o 2º número\n:"))
Numero3 = int(input("Introduza o 3º número\n:"))

if Numero1 > Numero2 and Numero1 > Numero3:
    print (f"O número {Numero1} é o maior") 
if Numero2 > Numero1 and Numero2 > Numero3:
    print (f"O número {Numero2} é o maior") 
if Numero3 > Numero1 and Numero3 > Numero1:
    print (f"O número {Numero3} é o maior") 
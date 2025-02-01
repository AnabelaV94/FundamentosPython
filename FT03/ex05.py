''' Escreva um programa que verifique se um determinado número introduzido pelo 
utilizador é nulo, positivo ou negativo. '''

Numero = int(input("Introduza o 1º número\n:"))

if Numero == 0:
    print (f"O número {Numero} é nulo") 
if Numero > 0:
    print (f"O número {Numero} é positivo") 
if Numero < 0:
    print (f"O número {Numero} é negativo") 
'''. Escreve um programa que receba dois números reais e indique qual o maior dos dois 
números. Considera a possibilidade de o utilizador indicar dois números iguais. '''


Numero1 = int(input("Introduza o 1º número\n:"))
Numero2 = int(input("Introduza o 2º número\n:"))

if Numero1 >= Numero2:
    print(f"O número {Numero1} é maior que o {Numero2}") 
else:
    print(f"O número {Numero2} é maior que o {Numero1}") 
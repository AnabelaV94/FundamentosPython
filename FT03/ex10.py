'''10. Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador 
deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores. 
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma 
mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da 
operação desejada. '''

Operacao = input("Introduza a operação que pretende realizar (+,-,*,/):")

Numero1 = int(input("Introduza o 1º número\n:"))
Numero2 = int(input("Introduza o 2º número\n:"))

if Operacao == "+":
    print(f"O valor é {Numero1+Numero2}") 
if Operacao == "-":
    print(f"O valor é {Numero1-Numero2}") 
if Operacao == "*":
    print(f"O valor é {Numero1*Numero2}") 
if Operacao == "/":
    print(f"O valor é {Numero1/Numero2}") 
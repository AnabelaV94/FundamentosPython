'''Escreve um programa que solicite um número inteiro ao utilizador e verifique se o 
mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato; 
"O número [número] é [par/ímpar]"'''

#Nota: um número é par quando o resto da divisão por 2 é zero. 

Numero = int(input("Introduza um número inteiro\n:"))
Resto = Numero % 2
#O operador % é chamado de "operador módulo", e ele retorna o resto da divisão inteira.

if Resto == 0:
    print(f"O número {Numero} é par") 
else:
    print(f"O número {Numero} é ímpar") 
    
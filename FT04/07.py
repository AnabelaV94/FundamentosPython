'''Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N)
 em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito 
utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não 
sabíamos a fórmula).'''

import os

os.system('cls' if os.name == 'nt' else 'clear')

Numero = int(input("Introduza o número\n:"))

# Inicializa a soma
soma = 0

# Percorre os números de 1 até Numero (incluindo Numero)
for i in range(1, Numero + 1):
    soma = soma + i  # Acumula a soma dos números naturais

# Exibe o resultado
print(f"A soma dos {Numero} primeiros números naturais é: {soma}")

#Outra resolução:

#n = ""
#while not n.lstrip('-').isdigit():
 #   n = input('Numero: ')

#n = int(n)
#n = None
#while n is None:
  #  try:
  #      n = int(input('Numero: '))
  #  except:
  #      n = None

#soma = 0
#for i in range(1, n+1):
   # soma += i 
#print(soma)
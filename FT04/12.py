'''Escreve um programa que calcule e escreva o resultado do fatorial de um número inteiro positivo N
 sabendo que: n!=1*2*3*…*n. '''
 
 # Pede ao utilizador para introduzir o número N
N = int(input("Introduza o número N: "))

Fatorial = 1
for i in range(1, N + 1):
     Fatorial *= i
print(f"o resultado do fatorial de um número inteiro positivo {N} é {Fatorial}")
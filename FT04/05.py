'''Elabora um programa para escrever no ecrã os números de 1 a 100.'''
# em python como fazer clear do terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

i = 0
while i < 100:
    soma = 1 + i
    print(f'{soma}')
    i +=1 
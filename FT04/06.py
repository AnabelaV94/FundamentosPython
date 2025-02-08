'''Elabora um programa para escrever no ecrã os números de 1 a 100 e os respetivos
 quadrados. '''
 
import os

os.system('cls' if os.name == 'nt' else 'clear')

i = 0
while i < 100:
    soma = 1 + i
    print(f'{soma} | {soma**2}')
    i += 1
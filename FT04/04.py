'''Escreve um programa para escrever no ecrã a palavra olá 100 vezes'''

# em python como fazer clear do terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

i = 1
while i <= 100:
    print(f'Olá')
    i +=1 
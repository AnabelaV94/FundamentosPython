'''Escreve um programa que calcule a soma dos 10 primeiros números inteiros positivos 
e devolva o resultado para o ecrã.'''

# Inicialização das variáveis
numero = 1
soma = 0
# Ciclo while para somar os 10 primeiros números inteiros positivos
while numero <= 10:
    soma =soma + numero
    numero += 1
# Exibição do resultado no ecrã
print("A soma dos 10 primeiros números inteiros positivos é:", soma)
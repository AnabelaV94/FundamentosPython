'''Escreva um programa que imprima os números de 1 até 50. '''

for num in range (1,51):
    print (num)

'''Utilizando estruturas de repetição escreva um programa que mostre os 
resultados da tabuada de multiplicação dos números entre 1 e 10, como segue.'''

for valor in range (1,11):
    for numero in range (1,11):
        print (f'{valor} x{numero}={valor*numero}')

''''''

import random
import statistics

# Gerar 100 números aleatórios entre 0 e 1
numeros = [random.random() for _ in range(100)]

# Calcular os valores solicitados
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = statistics.mean(numeros)
desvio_padrao = statistics.stdev(numeros)

# Exibir os resultados
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma dos números: {soma}")
print(f"Média: {media}")
print(f"Desvio padrão: {desvio_padrao}")

'''Escreva um programa que multiplique todos os elementos de uma lista.'''

lista = [10, 10, 10]
mul = 1

for num in lista:
    mul = mul * num  # Multiplica os elementos da lista

print(mul)  # Corrigido: deve imprimir "mul" em vez de "mul1"

'''Escreve um programa que ordene os elementos das listas a seguir em ordem 
crescente e decrescente.'''

 Listas fornecidas
lista1 = [117, 1519, 1335, 1600, 1676, 1491, 868, 1149, 642, 1321, 509, 1296, 1936, 1014,  
          1114, 1197, 94, 1347, 1112, 1224, 351, 1498, 1028, 255, 937, 514, 1041, 1923,  
          913, 510, 868, 1195, 1218, 1489, 1920, 630, 666, 605, 515, 1219, 59, 1217, 1293,  
          487, 1095, 1730, 1115, 1465, 1506, 1881]

lista2 = ['a', 'a', 'z', 'f', 'h', 'i', 'm', 'u', 'q', 'r', 'b', 'd']

# Ordenação crescente
lista1_crescente = sorted(lista1)
lista2_crescente = sorted(lista2)

# Ordenação decrescente
lista1_decrescente = sorted(lista1, reverse=True)
lista2_decrescente = sorted(lista2, reverse=True)

# Exibir os resultados
print("Lista1 em ordem crescente:", lista1_crescente)
print("Lista1 em ordem decrescente:", lista1_decrescente)

print("Lista2 em ordem crescente:", lista2_crescente)
print("Lista2 em ordem decrescente:", lista2_decrescente)

''' Escreve um programa, em python, que verifique se uma lista é vazia ou não. 
Caso a lista seja vazia, mostre True, caso contrário False.'''

lista = []  

if not len(lista) > 0:  
    print('Lista vazia')  
else:  
    print('A lista não é vazia')  
    
'''Crie um programa para controlar listas, com as seguintes funções:'''
    
# Lista com diferentes peças de sushi
lista_sushi = SushiList()

# Adicionar diferentes peças de sushi à lista
lista_sushi.adicionar_fim("Nigiri de Salmão")
lista_sushi.adicionar_fim("Makizushi de Atum")
lista_sushi.adicionar_fim("Temaki de Camarão")
lista_sushi.adicionar_inicio("Sashimi de Peixe Branco")
lista_sushi.adicionar_inicio("Ebi Nigiri (Salmão e Camarão)")
lista_sushi.adicionar_fim("Uramaki de Peixe Espada")

# Respostas às questões:

# Imprimir elementos da lista
lista_sushi.imprimir_lista()

# Tamanho da lista
print("\nTamanho da lista:", lista_sushi.tamanho_lista())

# Remover um elemento (por exemplo, "Makizushi de Atum")
lista_sushi.remover_elemento("Makizushi de Atum")
print("\nApós remoção de 'Makizushi de Atum':")
lista_sushi.imprimir_lista()

# Esvaziar a lista
lista_sushi.esvaziar_lista()
print("\nApós esvaziar a lista:")
lista_sushi.imprimir_lista()
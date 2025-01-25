'''Faz um programa que receba a distância em km e a quantidade em litros de 
combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve 
uma mensagem de acordo com o resultado obtido. (deverá ser criado o ficheiro 
ex07.py). '''

distância = float(input("introduza a distância percorrida\n"))
combustivel = float(input("introduza a quantidade em litros de combustível\n"))
valor_consumo= distância/combustivel
print (f" consumo km/l = {valor_consumo}")

# Mensagem baseada no valor do consumo
if valor_consumo < 8:
    print("Consumo muito alto!")
elif 8 <= valor_consumo <= 12:
    print("Consumo moderado.")
else:
    print("Consumo eficiente!")
'''Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a
converta para grau Celsius (C), devolvendo o resultado da conversão.
Use a fórmula: 
C = 5 * ((F-32) / 9).'''


Fahrenheit = int(input("Introduza a temperatura em Fahrenheit (F) \n:"))

Celsius = 5*((Fahrenheit-32) / 9)

print(f"A temperatura é Celsius (C) é {round(Celsius,2)}") 

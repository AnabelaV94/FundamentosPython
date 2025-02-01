'''Escreve um programa que calcule o volume de uma esfera. O valor do raio deverá ser  introduzido pelo utilizador 
(deverá ser criado o ficheiro ex04.py).'''
import math

raio = float(input("Introduz o valor do raio, pf \n"))
volume_esfera_numero = (4/3) * math.pi * (raio**3)  
print(f"Volume da esfera com o raio {raio} é {round(volume_esfera_numero,2)}")
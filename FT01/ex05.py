'''Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor 
da hipotenusa (deverá ser criado o ficheiro ex05.py).'''

import math

valor_a = float(input("Sejam a e b os catetos de um triângulo retângulo, introduza a\n"))
valor_b = float(input("Sejam a e b os catetos de um triângulo retângulo, introduza b\n"))
valor_hipotenusa = math.sqrt(valor_a**2+valor_b**2)
print (f"O valor da hipotenusa é {valor_hipotenusa}")
'''Escreve um programa para classificar um triângulo de acordo com o comprimento dos 
seus lados. Considere as seguintes informações: 
• Triângulo equilátero: todos os lados possuem o mesmo comprimento; 
• Triângulo escaleno: todos os lados possuem comprimento diferente; 
• Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento. '''

Lado1 = float(input("Introduza o comprimento do lado 1\n:"))
Lado2 = float(input("Introduza o comprimento do lado 2\n:"))
Lado3 = float(input("Introduza o comprimento do lado 3\n:"))

if Lado1 == Lado2 == Lado3:
    print (f"O ano triângulo é equilátero: todos os lados possuem o mesmo comprimento") 
elif Lado1 != Lado2 != Lado3:
    print (f"O ano triângulo é escaleno: todos os lados possuem comprimento diferente") 
else:
    print (f"O ano triângulo é isósceles: caracterizado por ter dois lados com o mesmo comprimento") 
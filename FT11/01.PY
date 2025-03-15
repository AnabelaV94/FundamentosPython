def triangulo (lado1,lado2,lado3):
    if  lado1==lado2 and lado2==lado3:
        return "Equilátero"
    elif lado1!=lado2 and lado2!=lado3 and lado1!=lado3:
        return "Escaleno"
    else:
        return "Isósceles"

a = float(input("Introduza medida de comprimento do lado 1!"))
b = float(input("Introduza medida de comprimento do lado 2!"))
c = float(input("Introduza medida de comprimento do lado 3!"))
       
res = triangulo(a,b,c)
print(res)
  

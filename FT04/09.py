''' Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número
 introduzido pelo utilizador. '''
 
Numero = int(input("Introduza o número\n:"))

# Percorre os números de 1 até 10
for i in range(1, 11):
    Resultado = Numero * i  # Calcula o produto do número e i
    # Exibe o resultado da tabuada
    print(f" {Numero} x {i} = {Resultado}")
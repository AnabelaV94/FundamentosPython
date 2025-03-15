
vera goncalves 12:28 PM
def tipo_triangulo(lados):
    # Verifica se foram inseridos exatamente 3 números
    if len(lados) != 3:
        return "Por favor, insira exatamente 3 números."
    
    # Verifica se todos os valores são números
    if not all(isinstance(i, (int, float)) for i in lados):
        return "Por favor, insira apenas números válidos para os lados do triângulo."
    
    # Verifica se os lados são positivos
    if any(i <= 0 for i in lados):
        return "Os lados devem ser maiores que zero!"
    
    # Atribui os lados para variáveis
    lado1, lado2, lado3 = lados
    
    # Verifica o tipo do triângulo
    if lado1 == lado2 == lado3:
        return "O triângulo é equilátero."
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return "O triângulo é isósceles."
    else:
        return "O triângulo é escaleno."
# Exemplo de uso:
print(tipo_triangulo([10,2,100]))
print(tipo_triangulo([102,100]))
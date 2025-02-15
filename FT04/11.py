# Pede ao utilizador para introduzir o número N
N = int(input("Introduza o número N: "))

# Inicializa a soma e o produto
soma = 0
produto = 1

# Percorre os números de 1 até N
for i in range(1, N + 1):
    soma += i  # Acumula a soma dos números naturais
    produto *= i  # Acumula o produto dos números naturais

# Exibe o resultado
print(f"A soma dos {N} primeiros números naturais é: {soma}")
print(f"O produto dos {N} primeiros números naturais é: {produto}")
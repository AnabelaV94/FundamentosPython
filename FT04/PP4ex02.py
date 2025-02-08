num1 = int(input("Digite o primeiro número inteiro: "))
operacao = input("Escolha a operação (+, -, *, /): ")
num2 = int(input("Digite o segundo número inteiro: "))

# Verificando a operação com o match
match operacao:
    case "+":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    case "/":
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado:.2f}")
    case _:
        print("Operação inválida! Escolha entre +, -, * ou /.")  
    
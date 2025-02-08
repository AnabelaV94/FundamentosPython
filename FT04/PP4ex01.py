#Programa que receba o nome de um produto e o seu preço e retorne o preço total considerando os descontos.
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
match produto:
    case "smartphone":
        print(f"Foi aplicado um desconto de {preco * 0.1} (10%) O valor a ser pago é: {preco - preco * 0.1}")
    case "tablet":
        print(f"Foi aplicado um desconto de {preco * 0.15} (15%) O valor a ser pago é: {preco - preco * 0.15}")
    case "laptop":
        print(f"Foi aplicado um desconto de {preco * 0.2} (20%) O valor a ser pago é: {preco - preco * 0.2}")
    case _:
        print("O produto selecionado não tem desconto associado, ovalor a ser pago é: ", preco)
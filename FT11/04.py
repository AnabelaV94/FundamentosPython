import builtins
class Cores:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
def print(*args, **kwargs):
    cor = kwargs.get('cor', Cores.RESET)
    end = kwargs.get('end', '\n')
    texto = ' '.join(map(str, args))
    fancy = cor + texto + Cores.END 
    builtins.__dict__['__original_print__'](fancy, end=end)  # evita recursão infinita
# guardar referência original da função print
builtins.__original_print__ = builtins.print
builtins.print = print  # substituir print por fprint
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
print("Triangulo Equilátero", cor=Cores.BLUE)

from minhasfunçoes import soma_media_numerodeelementos

num1 = int(input('Adiciona o primeiro numero'))
num2 = int(input('Adiciona o segundo numero'))
num3 = int(input('Adiciona o terceiro numero'))
num4 = int(input('Adiciona o quarto numero'))
resultado = soma_media_numerodeelementos(num1,num2,num3,num4)


minhasfunçoes.py
def soma_media_numerodeelementos (*num):
    
    soma = sum(num)
    quantidade = len(num)
    media = soma / quantidade
    
    
    print(f"Soma: {soma}")
    print(f"Número de elementos: {quantidade}")
    print(f"Média: {media:.2f}")
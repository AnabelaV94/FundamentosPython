from my_fancy_terminal import *

def quadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    output = f'Quadrado com lado {lado}'
    output += f'\n * Área: {area}'
    output += f'\n * Perímetro: {perimetro}'
    return output
# Testes
fprint(quadrado(1), cor=Cores.RED)  # Área: 1 Perímetro: 4
fprint(quadrado(2), cor=Cores.BLUE) # Área: 4 Perímetro: 8
fprint(quadrado(3), cor=Cores.RED)  # Área: 9 Perímetro: 12
fprint(quadrado(4), cor=Cores.BLUE) # Área: 16 Perímetro: 16
class Cores:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
def fprint(*args, **kwargs):
    
    # kargs
    cor = kwargs.get('cor', Cores.RESET)
    end = kwargs.get('end', '\n')
    # args
    texto = ' '.join(map(str, args))
    fancy = cor + texto + Cores.RESET 
    print(fancy, end=end)
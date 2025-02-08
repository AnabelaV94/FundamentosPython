'''Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de
 uma pessoa. '''
 
 
Numero = str(input("Introduza o seu estado civil (S, C, V) \n:"))

# Convertendo a entrada para maiúsculas para garantir que não importa se a pessoa digitar 's', 'c', 'v' em minúsculas
match Numero.upper():
    case 'S':
        print("Solteiro")
    case 'C':
        print("Casado")
    case 'V':
        print("Viúvo")
    case _:
        print("Informação inválida")
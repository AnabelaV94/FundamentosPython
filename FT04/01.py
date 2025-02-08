'''Faz um programa que escreva o nome do mês que é introduzido, pelo utilizador, na
 forma numérica. '''
 
# Solicita ao usuário para inserir o número do mês
Numero = int(input("Introduza de forma numérica o mês (1-12)\n:"))

# Usando match-case para determinar o nome do mês
match Numero:
    case 1:
        print("O {Numero} é Janeiro.")
    case 2:
        print("O {Numero} 2 é Fevereiro.")
    case 3:
        print("O {Numero} 3 é Março.")
    case 4:
        print("O {Numero} 4 é Abril.")
    case 5:
        print("O {Numero} 5 é Maio.")
    case 6:
        print("O {Numero} 6 é Junho.")
    case 7:
        print("O {Numero} 7 é Julho.")
    case 8:
        print("O {Numero} 8 é Agosto.")
    case 9:
        print("O {Numero} 9 é Setembro.")
    case 10:
        print("O {Numero} 10 é Outubro.")
    case 11:
        print("O {Numero} 11 é Novembro.")
    case 12:
        print("O {Numero} 12 é Dezembro.")
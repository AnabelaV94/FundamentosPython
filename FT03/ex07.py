'''Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser 
um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for 
divisível por 100. '''

Ano = int(input("Introduza o ano\n:"))
Ano2 = Ano % 400
Ano3 = Ano % 4
Ano4 = Ano % 100

if Ano2 == 0 or (Ano3 == 0 and Ano4 !=0):
    print (f"O ano {Ano} é o bissexto (tem 366 dias)", end=" ") 
else:
    print (f"O ano {Ano} não é um ano bissexto (tem 365 dias)", end=" ") 

if Ano == 2024:
     print (f".Para além disso é o ano atual!") 



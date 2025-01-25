'''Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e 
converta o resultado para segundos, devolvendo o output para o ecrã (deverá ser 
criado o ficheiro ex06.py).'''

valor_horas = int(input("introduza as horas\n"))
valor_minutos = int(input("introduza os minutos\n"))
valor_segundos = int(input("introduza os segundos\n"))
valor_final_segundos = (valor_horas * 3600) + (valor_minutos * 60) + valor_segundos
print (f" o valor em segundos é {valor_final_segundos}")

#infos: https://tortoisegit.org/
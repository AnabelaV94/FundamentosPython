'''Cria agora um nove ficheiro python (extensão .py) com o nome ex04.
Escreve um programa que solicite duas notas ([nota1] e [nota2]) ao utilizador e
apresente a média das mesmas da seguinte forma:
“A média das notas [nota1] e [nota2] é [média].”'''

import statistics

nota1 = int(input("Introduza a nota1\n:"))
nota2 = int(input("Introduza a nota2\n:"))

média = statistics.mean ([nota1, nota2])
print(f"A média das notas {nota1} e {nota2} é {média}") 
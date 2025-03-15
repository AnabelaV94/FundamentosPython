txt = """Python é uma linguagem de programação 
2 de 3 
de alto nível, interpretada de script, imperativa, orientada a objetos, 
funcional, de tipagem dinâmica e forte."""

# a) Imprimir o texto todo em maiúsculas
print("Texto em maiúsculas:")
print(txt.upper())

# b) Pedir uma palavra ao utilizador e verificar se está no texto
palavra = input("Digite uma palavra para verificar se está no texto: ")
if palavra in txt:
    print(f"A palavra '{palavra}' está no texto.")
else:
    print(f"A palavra '{palavra}' NÃO está no texto.")

# c) Imprimir o número de vezes que a letra ‘O’ ocorre no texto (maiúscula e minúscula)
contagem_o = txt.lower().count('o')
print(f"A letra 'O' ocorre {contagem_o} vezes no texto.")

# d) Substituir todas as ocorrências da letra ‘P’ no texto por ‘_’
txt_modificado = txt.replace('P', '_').replace('p', '_')
print("Texto modificado:")
print(txt_modificado)

'''outra resolução'''

txt="""Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte."""
# Imprimir o texto todo em maiusculas
print(txt.upper())
texto=txt.upper().split(" ")
palavra=input("Introduza uma palavra a verificar: ")
palavraProc=palavra.upper()
numeroPal=0
for x in texto:
    if palavraProc in x:
        numeroPal+=1
if numeroPal==0 :
    print(f"A palavra '{palavraProc}' não está presente no texto de análise")
else:
    print(f"A palavra '{palavraProc}' está presente no texto de análise {numeroPal} vezes")
vezesO=0
for x in texto:
    for letra in x:
        if 'O' in letra:
            vezesO+=1
texto1=txt.count("o")
print(f"A letra 'O' aparece {vezesO} vezes.")
print(f"A letra 'O' aparece {texto1} vezes.")
frase=txt.lower()
frase1=frase.replace("p","_")
print(frase1)
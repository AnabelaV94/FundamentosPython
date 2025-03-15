# b. Efetua a média de todos os valores inteiros na lista.
soma = 0
contador = 0
for num in nums:
    if type(num) == int:
        soma += num
        contador += 1
media = soma / contador
print(f'Média dos valores inteiros: {media}')
# c. Crie e retorne uma nova lista só com os valores inteiros
inteiros = [num for num in nums if type(num) == int]
print(f'Lista só com os valores inteiros: {inteiros}')


#versao 1: 
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]

#Alinea a)
c_int=0
c_float=0
c_str=0
c_bool=0
for x in nums:
    if type(x)==int:
        c_int=c_int+1
        continue
    if type(x)==float:
        c_float=c_float+1
        continue
    if type(x)==str:
        c_str=c_str+1
        continue
    if type(x)==bool:
        c_bool=c_bool+1
print("quantidade de inteiros na lista= ", c_int)
print("quantidade de floats na lista= ", c_float)
print("quantidade de Strings na lista= ", c_str)
print("quantidade de Booleanos na lista= ", c_bool)
#Alinea b)
soma=0
count=0
for x in nums:
    if type(x)==int:
        soma = soma +x
        count=count+1
media=soma/count
print("A media dos valores inteiros é: ", media)
#Alinea c)
nova_lista=[]
for x in nums:
    if type(x)==int:
        nova_lista.append(x)

print(nova_lista)


#versao2 Lista inicial
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]
# a. Conta a quantidade de cada tipo de dado
inteiros = len([x for x in nums if isinstance(x, int) and not isinstance(x, bool)])

floats = sum(1 for x in nums if isinstance(x, float))
strings = sum(1 for x in nums if isinstance(x, str))
booleanos = sum(1 for x in nums if isinstance(x, bool))
print(f"Inteiros: {inteiros}, Floats: {floats}, Strings: {strings}, Booleanos: {booleanos}")
# b. Calcula a média dos inteiros
valores_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
media = sum(valores_inteiros) / len(valores_inteiros)
print(media)
# c. Cria uma nova lista só com os inteiros
lista_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
print(lista_inteiros)
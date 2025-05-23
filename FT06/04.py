nums = [10, 2.5, 7, 11, 7.9, 'Python', True, 6, 5.8, 'Listas']
# a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
inteiros = 0
floats = 0
strings = 0
boleanos = 0
# Usando for loop & type
for num in nums:
    if type(num) == int:
        inteiros += 1
    elif type(num) == float:
        floats += 1
    elif type(num) == str:
        strings += 1
    elif type(num) == bool:
        boleanos += 1
# (EXTRA) Usando list comprehension
inteiros = len([ num for num in nums if type(num) == int   ])
floats   = len([ num for num in nums if type(num) == float ])
strings  = len([ num for num in nums if type(num) == str   ])
boleanos = len([ num for num in nums if type(num) == bool  ])

print(f'Quantidade de inteiros: {inteiros}')
print(f'Quantidade de floats: {floats}')
print(f'Quantidade de strings: {strings}')
print(f'Quantidade de boleanos: {boleanos}')
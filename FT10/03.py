# String com as datas separadas por ","
datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

# a) Armazenar as diferentes datas numa lista
lista_datas = datas.split(",")

# b) Imprimir as datas correspondentes ao ano de 2022
print("Datas do ano de 2022:")
for data in lista_datas:
    if "2022" in data:
        print(data)

# c) Criar uma nova lista (dias) e armazenar o dia de cada data
dias = [data[:2] for data in lista_datas]  # Extrai os dois primeiros caracteres (dia)
dias.sort()  # Ordenar a lista de forma crescente

# Imprimir a lista ordenada
print("Lista de dias ordenada:", dias)



'''resolução adicional'''

#a) Armazene as diferentes datas numa string;
dates = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
#b) Imprima as datas correspondentes ao ano de 2022;
date_list = dates.split(",")
print(date_list)
for x in date_list:
    if x[-4:] == '2022':
        print(x)
output = [x for x in date_list if x[-4:] == '2022']
print(output)
#c) Crie uma nova lista (dias) e na mesma armazena o dia de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
days = []
for x in date_list:
    days.append(int(x[:2]))
print(days)
days_sorted = sorted(days)
print(days_sorted)
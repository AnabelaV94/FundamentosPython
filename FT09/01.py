menu={
    "entremeada": 7,
    "Sardinha": 6,
    "Filetes": 5.5,
    "Prego": 7,
    "Hamburguer": 5.5
}
# Devolva o preço do “prego”
p_prego = menu.get("Prego")
print ("O preço do prego é: ", p_prego)
# Faça o print de todas as chaves do dicionário
print (menu.keys())
# Acrescente na lista “omolete” com o preço de 5
menu.update({"Omelete ": 5})
# Faça o print de todo o dicionário, para visualizar as alterações.
for x, y in menu.items():
    print(x , y)
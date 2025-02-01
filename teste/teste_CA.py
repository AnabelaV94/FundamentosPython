


import pandas as pd
#from thefuzz import process  

# 📌 1. Carregar a base de referência dos associados (com Nome_Entidade e NIF)
df_associados = pd.read_excel("C:\\Users\\Anabela Veiga\\Desktop\\HCP - 06.11.23.xlsx")
print("📄 df_associados (Associados) carregado com sucesso!")
print(df_associados.head())  # Mostra as 5 primeiras linhas

# 📌 2. Carregar a lista de inscritos do evento (com Nome_Entidade)
df_evento = pd.read_excel("C:\\Users\\Anabela Veiga\\Desktop\\DIRETÓRIO_Associados_janeiro2025.xlsx")  
print("📄 df_evento (Evento) carregado com sucesso!")
print(df_evento.head())  # Mostra as 5 primeiras linhas

# Criar um dicionário {Nome_Entidade: NIF} para referência
associados_dict = dict(zip(df_associados["Nome_Entidade"], df_associados["NIF"]))

# 📌 3. Função para encontrar a melhor correspondência usando fuzzy matching
#def encontrar_nif(nome):
    #match, score = process.extractOne(nome, associados_dict.keys())  # Melhor correspondência
    #if score > 80:  # Se a similaridade for maior que 80%
    #    return associados_dict[match]  # Retorna o NIF correspondente
   # return None  # Caso contrário, retorna None (valor em branco no Excel)

# 📌 4. Aplicar a função para adicionar a coluna NIF
#df_evento["NIF"] = df_evento["Nome_Entidade"].apply(encontrar_nif)

# 📌 5. Adicionar a coluna "Associado" (Sim se tiver NIF, Não se estiver em branco)
#df_evento["Associado"] = df_evento["NIF"].apply(lambda x: "Sim" if pd.notna(x) else "Não")

# 📌 6. Salvar os resultados
#df_evento.to_excel("evento_com_nif.xlsx", index=False)

#print("Processo concluído! Arquivo salvo como 'evento_com_nif.xlsx'.")

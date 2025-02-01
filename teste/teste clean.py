import pandas as pd
from thefuzz import process  

# 📌 1. Carregar a base de associados
df_associados = pd.read_excel("C:\\Users\\Anabela Veiga\\Desktop\\DIRETÓRIO_Associados_janeiro2025.xlsx", header=1)
df_associados.columns = df_associados.columns.str.strip()  # Remover espaços extras
print("📄 Column names in df_associados:", df_associados.columns.tolist())

# 📌 Criar dicionário {Nome_Entidade: NIF}
associados_dict = dict(zip(df_associados["Nome_Entidade"], df_associados["NIF"]))

# 📌 2. Carregar a lista de inscritos do evento
df_evento = pd.read_excel("C:\\Users\\Anabela Veiga\\Desktop\\HCP - 06.11.23.xlsx", header=0)  
df_evento.columns = df_evento.columns.str.strip()  # Remover espaços extras
print("📄 Column names in df_evento:", df_evento.columns.tolist())

# 📌 3. Função para encontrar a melhor correspondência e retornar NIF + Nome_Entidade correspondente
def encontrar_nif(nome):
    if not nome or not isinstance(nome, str):  # Verificar se a entrada é válida
        return None, None

    resultado = process.extractOne(nome, associados_dict.keys())  # Melhor correspondência
    if resultado:
        match, score = resultado  # Nome correspondente + Score de similaridade
        if score >= 80:  # Se a similaridade for maior que 80%
            return associados_dict[match], match  # Retorna o NIF e o Nome_Entidade correspondente
    return None, None  # Caso contrário, retorna None para ambos

# 📌 4. Aplicar a função para obter o NIF e o Nome_Entidade correspondente
df_evento[["NIF", "Nome_Entidade Correspondente"]] = df_evento["Organization"].apply(lambda nome: pd.Series(encontrar_nif(nome)))

# 📌 5. Criar a coluna "Associado" com "Associado" se houver NIF, ou vazio se não houver
df_evento["Associado"] = df_evento["NIF"].apply(lambda x: "Associado" if pd.notna(x) else "")

# 📌 6. Mostrar resultados
print("✅ Correspondências encontradas:")
print(df_evento[["Organization", "Nome_Entidade Correspondente", "NIF", "Associado"]].head())

# 📌 7. Guardar o resultado num novo ficheiro Excel
output_path = "C:\\Users\\Anabela Veiga\\Desktop\\eventos_com_nif.xlsx"
df_evento.to_excel(output_path, index=False)
print(f"✅ Ficheiro salvo com sucesso em: {output_path}")

import pandas as pd
from thefuzz import process

# 📌 1. Carregar a base de associados
df_associados = pd.read_excel("C:\\Users\\Anabela Veiga\\Desktop\\DIRETÓRIO_Associados_janeiro2025_.xlsx", header=1)
df_associados.columns = df_associados.columns.str.strip()  # Remover espaços extras
print("📄 Column names in df_associados:", df_associados.columns.tolist())

# Criar dicionário {Entidade: (NIF, Estado Atual)}
associados_dict = dict(zip(df_associados["Entidade"], zip(df_associados["NIF"], df_associados["Estado Atual"])))

# 📌 2. Carregar a lista de inscritos do evento
df_evento = pd.read_excel("C:\\Users\\Anabela Veiga\\Desktop\\HCP - 06.11.23.xlsx", header=0)
df_evento.columns = df_evento.columns.str.strip()  # Remover espaços extras
print("📄 Column names in df_evento:", df_evento.columns.tolist())

# 📌 3. Função para encontrar a melhor correspondência e retornar NIF + Entidade correspondente + Status
def encontrar_info(nome):
    if not nome or not isinstance(nome, str):  # Verificar se a entrada é válida
        return None, None, "Não Associado"
    
    resultado = process.extractOne(nome, associados_dict.keys())  # Melhor correspondência
    if resultado:
        match, score = resultado  # Nome correspondente + Score de similaridade
        if score >= 80:  # Se a similaridade for maior que 80%
            nif, estado = associados_dict[match]  # Obtém NIF e estado atual
            associado_status = "Associado" if estado == "ok" else "Não Associado"
            return nif, match, associado_status
    return None, None, "Não Associado"  # Caso contrário, retorna valores padrão

# 📌 4. Aplicar a função para obter as informações correspondentes
df_evento[["NIF", "Entidade", "Associado"]] = df_evento["Organization"].apply(lambda nome: pd.Series(encontrar_info(nome)))

# 📌 5. Mostrar resultados
print("✅ Correspondências encontradas:")
print(df_evento[["Organization", "Entidade", "NIF", "Associado"]].head())

# 📌 6. Guardar o resultado num novo ficheiro Excel
output_path = "C:\\Users\\Anabela Veiga\\Desktop\\eventos_atualizado.xlsx"
df_evento.to_excel(output_path, index=False)
print(f"✅ Ficheiro salvo com sucesso em: {output_path}")
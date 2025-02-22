import pandas as pd

# Definir o caminho completo para o ficheiro
filename_in = 'C:/Users/Anabela Veiga/Desktop/Python/Teste.xlsx'
filename_out = filename_in.replace('.xlsx', '_clean.xlsx')

# Ler o ficheiro Excel
df = pd.read_excel(filename_in)

# Limpar as barras em todas as colunas
for col in df.columns:
    for i, value in enumerate(df[col]):
        if isinstance(value, str):  # A função de replace funciona apenas em strings
            df[col][i] = value.replace('\\', '')

# Mostrar o início do DataFrame
print(df.head())

# Guardar o DataFrame limpo
df.to_excel(filename_out, index=False)
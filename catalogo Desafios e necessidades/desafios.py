import pandas as pd

# Caminho para o arquivo Excel original
arquivo_excel = r"C:\Users\Anabela Veiga\Downloads\Copy of Catálogo 21.30.25.xlsx"

# Ler a aba "Catálogo de Entidades_desafios"
df = pd.read_excel(arquivo_excel, sheet_name="Catálogo de Entidades_desafios")

# Lista pré-definida dos 16 desafios (excetuando "Outros")
predef_desafios = [
    "Processos de certificação e autorização no mercado",   # 1
    "Acesso a Linhas de Financiamento",                       # 2
    "Desconhecimento da Regulamentação",                      # 3
    "Acesso a validação em ambiente real",                    # 4
    "Internacionalização",                                    # 5
    "Crescimento por aumento de pipeline/ diversificação de produtos e/ou serviços",  # 6
    "Crescimento por aumento de volume nacional",           # 7
    "Concorrência nacional",                                  # 8
    "Concorrência internacional",                             # 9
    "Entrada no mercado",                                     # 10
    "Encontrar clientes",                                     # 11
    "Acesso a Recursos humanos especializados",             # 12
    "Acesso a Redes de conhecimento",                         # 13
    "Controlo de qualidade",                                  # 14
    "Acesso a infraestruturas laboratoriais",                 # 15
    "Crescimento por aumento de volume internacional"        # 16
]

# Nome da coluna para os itens que não correspondem às categorias pré-definidas
nome_outros = "Outros que nao encaixem nestas categorias"

# Função para dividir a coluna "Desafios Principais*"
def split_desafios(valor):
    if pd.isna(valor) or valor.strip() in ["", "-"]:
        return []  # Se não houver informação, retorna lista vazia
    # Divide pelo separador vírgula e remove espaços extras; ignora entradas vazias
    return [d.strip() for d in valor.split(",") if d.strip()]

# Criar uma coluna auxiliar com a lista de desafios para cada linha
df["desafios_list"] = df["Desafios Principais*"].apply(split_desafios)

# Para cada um dos 16 desafios pré-definidos, cria uma coluna:
for desafio in predef_desafios:
    df[desafio] = df["desafios_list"].apply(
        lambda lista: desafio if any(d.lower() == desafio.lower() for d in lista) else ""
    )

# Para a coluna "Outros", pegar os itens que não correspondem a nenhum dos 16 desafios pré-definidos
def extrair_outros(lista):
    outros = []
    for item in lista:
        if not any(item.lower() == desafio.lower() for desafio in predef_desafios):
            outros.append(item)
    return ", ".join(outros)

df[nome_outros] = df["desafios_list"].apply(extrair_outros)

# (Opcional) Remover a coluna auxiliar
df.drop(columns=["desafios_list"], inplace=True)

# (Opcional) Salvar o DataFrame processado em um novo arquivo Excel
saida_excel = r"C:\Users\Anabela Veiga\Downloads\Catálogo_Processado.xlsx"
df.to_excel(saida_excel, index=False)

print("Processamento concluído! O arquivo foi salvo em:", saida_excel)

import pandas as pd

# Caminhos para os arquivos
arquivo_excel = r"C:\Users\Anabela Veiga\Downloads\Copy of Catálogo 21.30.25.xlsx"
saida_excel = r"C:\Users\Anabela Veiga\Downloads\Catálogo_Processado_Necessidades.xlsx"

# Ler a aba "Catálogo de Entidades_necessida"
df_nec = pd.read_excel(arquivo_excel, sheet_name="Catálogo de Entidades_necessida")

# Lista pré-definida das 17 categorias de necessidades (excetuando o "Outros")
predef_nec = [
    "Inteligência Artificial e Machine Learning em Saúde",
    "Interoperabilidade e Gestão de Dados",
    "Value-Based Health Care (VBHC)",
    "Financiamento e fundos públicos e privados",
    "Propriedade Intelectual",
    "Gestão da Inovação e Transferência de Tecnologia",
    "Comunicação e relações públicas",
    "Desenvolvimento de negócio",
    "Design/usabilidade de soluções tecnológicas",
    "Assuntos regulamentares e certificação",
    "Geração de evidência e ensaios clínicos",
    "Liderança",
    "Ecossistemas de inovação e parcerias",
    "Medical writing",
    "Requisitos éticos",
    "Gestão empresarial",
    "Controlo de qualidade e validação de resultados"
]

# Nome da coluna para os itens que não se enquadram nas categorias pré-definidas
nome_outros = "Outros ( que diz respeito aquelas que nao se encaixam nas anteriores)"

# Função para dividir a coluna "Necessidades de capacitação prioritária*"
def split_necessidades(valor):
    if pd.isna(valor) or valor.strip() in ["", "-"]:
        return []  # Retorna lista vazia se não houver informação
    # Divide a string pela vírgula, removendo espaços e ignorando entradas vazias
    return [d.strip() for d in valor.split(",") if d.strip()]

# Criar uma coluna auxiliar com a lista de necessidades para cada linha
df_nec["nec_list"] = df_nec["Necessidades de capacitação prioritária*"].apply(split_necessidades)

# Para cada categoria pré-definida, criar uma coluna que indique se a entidade selecionou a opção
for categoria in predef_nec:
    df_nec[categoria] = df_nec["nec_list"].apply(
        lambda lista: categoria if any(item.lower() == categoria.lower() for item in lista) else ""
    )

# Para a coluna "Outros", coletar os itens que não correspondem a nenhuma das categorias pré-definidas
def extrair_outros(lista):
    outros = []
    for item in lista:
        if not any(item.lower() == categoria.lower() for categoria in predef_nec):
            outros.append(item)
    return ", ".join(outros)

df_nec[nome_outros] = df_nec["nec_list"].apply(extrair_outros)

# Remover a coluna auxiliar
df_nec.drop(columns=["nec_list"], inplace=True)

# (Opcional) Salvar o DataFrame processado em um novo arquivo Excel
df_nec.to_excel(saida_excel, index=False)

print("Processamento concluído!")
print("Arquivo salvo em:", saida_excel)

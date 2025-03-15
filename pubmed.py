import pandas as pd
from Bio import Entrez
from datetime import date
import os

# Define seu e-mail (obrigatório para uso da API)
Entrez.email = "aveiga@healthportugal.com"  # Substitua pelo seu e-mail válido

# Lista de entidades a pesquisar
entidades = [
    "Universidade Católica Portuguesa",
    "iLoF",
    "Fraunhofer Portugal"
]

# Calcula as datas para os últimos 10 anos
hoje = date.today()
dez_anos_atras = date(hoje.year - 10, hoje.month, hoje.day)
mindate_str = dez_anos_atras.strftime("%Y/%m/%d")
maxdate_str = hoje.strftime("%Y/%m/%d")

# Dicionário para armazenar os detalhes dos artigos por entidade
detalhes_por_entidade = {}
# Lista para armazenar o resumo (nome da entidade e total de publicações)
resumo = []

for entidade in entidades:
    print(f"Pesquisando para: {entidade}")
    term = entidade  # Você pode ajustar o termo de busca, ex: f"{entidade}[Affiliation]"

    # Realiza a busca no PubMed, limitando as publicações aos últimos 10 anos
    handle = Entrez.esearch(
        db="pubmed",
        term=term,
        retmax=10000,
        mindate=mindate_str,
        maxdate=maxdate_str,
        datetype="pdat"  # Filtra pela data de publicação
    )
    record = Entrez.read(handle)
    handle.close()
    
    total_publicacoes = int(record["Count"])
    id_list = record["IdList"]
    
    # Adiciona ao resumo a entidade e o número total de publicações encontradas
    resumo.append({
        "Entidade": entidade,
        "Numero total de publicacoes": total_publicacoes
    })
    
    detalhes_artigos = []
    if id_list:
        # Busca os detalhes dos artigos (formato XML)
        handle = Entrez.efetch(db="pubmed", id=id_list, rettype="xml")
        records = Entrez.read(handle)
        handle.close()
        
        for article in records['PubmedArticle']:
            medlineCitation = article.get('MedlineCitation', {})
            artigo = medlineCitation.get('Article', {})
            
            # Extrai o título do artigo
            titulo = artigo.get('ArticleTitle', 'N/D')
            
            # Extrai a(s) categoria(s) de publicação
            pub_types = artigo.get('PublicationTypeList', [])
            categoria = ", ".join(pub_types) if pub_types else "N/D"
            
            # Extrai a data de publicação a partir de JournalIssue -> PubDate
            journal_issue = artigo.get('Journal', {}).get('JournalIssue', {})
            pub_date = journal_issue.get('PubDate', {})
            ano = pub_date.get('Year', 'N/D')
            mes = pub_date.get('Month', '')
            dia = pub_date.get('Day', '')
            data_publicacao = " ".join(filter(None, [dia, mes, ano])).strip()
            
            detalhes_artigos.append({
                "Nome artigo": titulo,
                "Categoria de artigo": categoria,
                "Data de publicacao": data_publicacao
            })
    
    # Armazena os detalhes para a entidade atual
    detalhes_por_entidade[entidade] = detalhes_artigos

# Define o caminho para salvar o arquivo Excel na área de trabalho
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
caminho_excel = os.path.join(desktop, "resultados_pubmed.xlsx")

# Cria o arquivo Excel com várias abas:
# - Aba "Resumo" com a entidade e o número total de publicações
# - Uma aba para cada entidade com os detalhes dos artigos
with pd.ExcelWriter(caminho_excel) as writer:
    # Aba Resumo
    df_resumo = pd.DataFrame(resumo)
    df_resumo.to_excel(writer, sheet_name="Resumo", index=False)
    
    # Abas para cada entidade (nome da aba limitado a 31 caracteres)
    for entidade, detalhes in detalhes_por_entidade.items():
        df_detalhes = pd.DataFrame(detalhes)
        sheet_name = entidade[:31]
        df_detalhes.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Extração concluída. Dados salvos em '{caminho_excel}'.")

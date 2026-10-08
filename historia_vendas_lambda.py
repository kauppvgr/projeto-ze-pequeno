#importando as bibliotecas

import pandas as pd
import datetime as dt

#carregando a planilha Zé Pequeno
df = pd.read_excel('tabela_vendas_ZePequeno_LIMPA.xlsx')

#tratamento dos dados
df["Valor_Venda"] = df["Valor_Venda"].apply(lambda x: float(x) if pd.notnull(x) and x != "" else 0.0)


#Regra 1 = Classifica transações em "Boa Venda" ou "Venda Padrão" comparando com o valor médio
media_vendas = df["Valor_Venda"].mean()
df["Classificacao_Venda"] = df["Valor_Venda"].apply(
    lambda valor: "Boa Venda" if valor > media_vendas else "Venda Padrão")

#Regra 2 = Faz a limpeza e padronização dos textos da coluna Produto
df["Produto_Normalizado"] = df["Produto"].apply(lambda nome: str(nome).strip().title())

#Regra 3 = Formata o registo da coluna Data para exibir apenas o mês e o ano no formato MM/AAAA
df["Mes_Ano"] = df["Data"].apply(lambda d: d.strftime("%m/%Y"))

#Storytelling
print("=" * 50)
print("HISTÓRIA DE VENDAS - ZÉ PEQUENO PAÇOCAS E ROLHAS")
print("=" * 50)

#Análise 1 = Calcula o faturamento total acumulado por produto e exibe no terminal qual deles vendeu mais
vendas_produto = df.groupby("Produto_Normalizado")["Valor_Venda"].sum()
top_produto = vendas_produto.idxmax()
print(f"\nProduto Campeão:")
print(f"O produto que mais vendeu foi '{top_produto}', somando um total de R$ {vendas_produto[top_produto]:,.2f}.")

#Análise 2 = Compara as vendas entre os canais e imprime qual deles gerou mais receita
vendas_canal = df.groupby("Canal")["Valor_Venda"].sum()
top_canal = vendas_canal.idxmax()
print(f"\n2. Canal Dominante:")
print(f"O canal com maior receita foi '{top_canal}', acumulando R$ {vendas_canal[top_canal]:,.2f}.")

#Análise 3 = Filtra apenas as vendas de alto valor e descobre qual região registrou a maior quantidade dessas vendas
boas_vendas = df[df["Classificacao_Venda"] == "Boa Venda"]
contagem_regiao = boas_vendas.groupby("Região")["Valor_Venda"].count()
top_regiao = contagem_regiao.idxmax()
qtd_top = contagem_regiao[top_regiao]
print(f"\n3. Foco das Boas Vendas:")
print(f"As melhores transações (acima de R$ {media_vendas:,.2f}) concentraram-se em '{top_regiao}', com {qtd_top} vendas qualificadas.")

#Análise 4 = Calcula mês de maior faturamento
vendas_mes = df.groupby("Mes_Ano")["Valor_Venda"].sum()
melhor_mes = vendas_mes.idxmax()
print(f"\n4. Desempenho Temporal:")
print(f"O mês com maior volume de faturamento foi '{melhor_mes}', totalizando R$ {vendas_mes[melhor_mes]:,.2f}.")

print("\n" + "=" * 65)
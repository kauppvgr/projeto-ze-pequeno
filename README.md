# Projeto Zé Pequeno Paçocas e Rolhas 🥜🍾

Projeto prático desenvolvido para análise exploratória de dados de vendas utilizando a biblioteca **Pandas** e funções **Lambda** em Python.

## 📌 Objetivo do Projeto
Demonstrar a aplicação de regras de negócio, tratamento e transformação de dados de transações comerciais sem recorrer a funções tradicionais extensas, gerando uma narrativa analítica (storytelling) dos resultados diretamente no terminal.

## 🛠️ Tecnologias e Bibliotecas
* **Python**
* **Pandas** (leitura, transformação, agrupamento e agregação de dados)
* **Datetime** (manipulação de registos temporais)

## ⚙️ Regras de Negócio Implementadas (Funções Lambda)

1. **Classificação de Vendas (`Classificacao_Venda`):**
   * Classifica dinamicamente cada transação como `"Boa Venda"` se o montante for superior à média global de faturamento, ou `"Venda Padrão"` caso contrário.
2. **Normalização de Produtos (`Produto_Normalizado`):**
   * Limpa espaços indesejados (`strip()`) e padroniza a capitalização das palavras (`title()`), garantindo a consistência na agregação dos itens.
3. **Extração Temporal (`Mes_Ano`):**
   * Converte a data da transação para o padrão textual `MM/AAAA` através de `strftime()`, viabilizando análises de desempenho mês a mês.

---

## 📊 Histórias de Negócio Analisadas (Storytelling)

* **1. Produto Campeão:** Identifica o produto com maior receita acumulada no período avaliado.
* **2. Canal Dominante:** Compara os canais de distribuição (ex.: E-commerce vs. Loja Física) e indica qual gerou maior volume financeiro.
* **3. Foco das Boas Vendas:** Identifica a região geográfica que concentrou o maior volume de vendas qualificadas acima da média.
* **4. Desempenho Temporal:** Apresenta o mês que obteve o pico de faturação na operação.

---

## 🚀 Como Executar o Projeto

1. Abra o terminal do VS Code.
2. Instale as bibliotecas necessárias:
   pip install pandas openpyxl
3. Rode o scrip t de vendas digitando o comando abaixo e apertando Enter:
   python historia_vendas_lambda.py
4. Veja os resultados das histórias de vendas impressos diretamente na tela do terminal.

## 👩‍💻 Autoria
* **Desenvolvido por:** <span style="color: #8A2BE2;"><b>Vitória</b></span>

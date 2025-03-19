import pandas as pd


# Carregamento do arquivo marketing.csv
marketing = pd.read_csv("marketing.csv")

# Exibir as primeiras linhas do DataFrame para verificar a importação
print(marketing.head())
print(marketing.describe(include='all'))

# c) Imprima os tipos de dados das colunas e a quantidade de valores não nulos por coluna
print(marketing.info())
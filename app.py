import pandas as pd

import matplotlib.pyplot as plt


# Carregamento do arquivo marketing.csv
marketing = pd.read_csv("marketing.csv")

# Exibir as primeiras linhas do DataFrame para verificar a importação
print(marketing.head())
print(marketing.describe(include='all'))

# c) Imprima os tipos de dados das colunas e a quantidade de valores não nulos por coluna
print(marketing.info())

# Agrupar por 'date_served' e contar usuários únicos
daily_users = marketing.groupby('date_served')['user_id'].nunique()

# Exibir as primeiras linhas
print(daily_users.head())
daily_users.plot(kind='line', figsize=(10, 5))

# Adicionando título e rótulos dos eixos
plt.title('Usuários diários')
plt.ylabel('Número de usuários')

# Rotacionando os rótulos do eixo x para melhor visualização
plt.xticks(rotation=45)

# Exibindo o gráfico
plt.show()
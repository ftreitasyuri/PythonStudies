# Importar a base de dados
import pandas as pd

tabela_vendas = pd.read_excel("BasesDados/Vendas.xlsx")

# Visualizar a base de dados

pd.set_option('display.max_columns', None)
# print(tabela_vendas)

# Filtrando duas colunas 1ª forma
# tabela_vendas = tabela_vendas[['ID Loja', 'Valor Final']]
# print(tabela_vendas)





import pandas as pd

df = pd.read_excel('planilha_teste.xlsx', sheet_name='Plan1')
print(df, "\n\n")

#df.head traz as primeiras 5 linhas da planilha
#df.tail traz as ultimas linhas

#Traz informações das tabelas informadas
# pd = df[['NOME', 'IDADE']]
# print(pd)

# Traz informações as pessoas que tem a idade menor de 30 
dp = df[df['IDADE'] > 30]
print(dp)
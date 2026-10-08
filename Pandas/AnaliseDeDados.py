#importando o pandas
import pandas as pd

#Gerando dataFrames e Series
Dados = {
    "Nome": ["Mateus", "Felipe", "Daniel"],
    "Idade": [20, 30, 27]
}

df = pd.DataFrame(Dados)
s = pd.Series(Dados)

print(df, "\n\n") #Dividido em colunas
print(s) #DIvidido em índices, utilizando linhas e colunas
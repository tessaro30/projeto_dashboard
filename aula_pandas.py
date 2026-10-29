import pandas as pd

df = pd.read_excel("YDUQ3_evolucao.xlsx")
# Selecionando a coluna "valor" e aplicando funcoes estatisticas
print(df)
df["valor"].max()
df["valor"].min()
df["valor"].mean()
df["valor"].std()
# selecionar linhas
df[0:1]
# selecionar linhas e colunas
colunas = ["conta", "valor"]
df[23:24][colunas]
# filtrar linhas atraves valor
linhas = df["trimestre"] == "20262T"
colunas = ["conta", "valor"]
df[linhas][colunas]
# linha
linhas = df["conta"] == "lucro"
colunas = ["valor"]
df[linhas][colunas].mean()
# graficos
import seaborn as sns
import matplotlib.pyplot as plt
# grafico do lucro
linhas = df["conta"] == "lucro"
colunas = ["trimestre","valor"]
dados = df[linhas][colunas]
sns.lineplot(dados, x='trimestre', y='valor')
plt.title("grafico do lucro")
plt.xticks(rotation=45)

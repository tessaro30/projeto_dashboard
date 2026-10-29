import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
df = pd.read_excel("YDUQ3_evolucao.xlsx")
# grafico do lucro
linhas = df["conta"] == "lucro"
colunas = ["trimestre","valor"]
dados = df[linhas][colunas]
fig, ax = plt.subplots()
sns.lineplot(dados, x='trimestre', y='valor')
ax.set_title("grafico do lucro")
# plotar no dashboard do streamlit
tab1, tab2 = st.tabs(["tab 1", "tab 2"])
with tab1:
    st.title("dashboard da empresa YDUQS")
    st.pyplot(fig)
    st.dataframe(df)

with tab2:
    df = pd.read_excel("planilhao_b3.xlsx")
    st.dataframe(df)
    df_size = df.groupby("setor").size()
    fig, ax = plt.subplots()
    sns.barplot(df_size)
    ax.set_title("grafico do numero de empresas por setor")
    st.pyplot(fig)


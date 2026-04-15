import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# conexão com o banco
engine = create_engine("postgresql://iotuser:123456@localhost:5432/iotdb")

st.title("📡 Dashboard IoT - Monitoramento de Temperatura")

st.write("Análise de dados coletados por sensores IoT.")

# função para carregar dados
def load_data(query):
    return pd.read_sql(query, engine)

# --- média por sala
st.header("Temperatura média por sala")

df_sala = load_data("SELECT * FROM avg_temp_por_sala")

fig1 = px.bar(
    df_sala,
    x="sala",
    y="media_temperatura",
    title="Temperatura Média por Sala"
)

st.plotly_chart(fig1)

# --- dentro vs fora
st.header("Temperatura média dentro vs fora")

df_inout = load_data("SELECT * FROM avg_temp_in_out")

fig2 = px.bar(
    df_inout,
    x="ambiente",
    y="media_temperatura",
    title="Temperatura Média - Ambiente Interno vs Externo"
)

st.plotly_chart(fig2)

# --- quantidade de leituras
st.header("Quantidade de leituras por sala")

df_leituras = load_data("SELECT * FROM leituras_por_sala")

fig3 = px.bar(
    df_leituras,
    x="sala",
    y="total_leituras",
    title="Total de Leituras por Sala"
)

st.plotly_chart(fig3)
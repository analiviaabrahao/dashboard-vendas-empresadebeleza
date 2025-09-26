import streamlit as st
import pandas as pd
import altair as alt
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# --- Carrega variáveis do .env ---
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# --- Conexão com o banco ---
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# --- Título do dashboard ---
st.title("Dashboard de Vendas - Empresa de Beleza 💄")
st.markdown("Visualização de KPIs, receitas, ticket médio e rankings de produtos.")

# ---  Receita por categoria ---
query = """
SELECT DATE(v.order_date) AS data, p.categoria, SUM(v.quantidade) AS total_quantidade, SUM(v.preco_unitario * v.quantidade) AS receita
FROM vendas v
JOIN produtos p ON v.product_id = p.product_id
GROUP BY data, p.categoria
ORDER BY data;
"""
df = pd.read_sql(query, engine)

categoria_selecionada = st.selectbox("Selecione a categoria:", df["categoria"].unique())
df_filtrado = df[df["categoria"] == categoria_selecionada]

# KPIs em colunas
total_receita = df_filtrado["receita"].sum()
total_itens = df_filtrado["total_quantidade"].sum()
ticket_medio = total_receita / total_itens if total_itens else 0

st.subheader(f"KPI - Categoria: {categoria_selecionada}")
col1, col2, col3 = st.columns(3)
col1.metric("💰 Receita Total", f"R$ {total_receita:,.2f}")
col2.metric("📦 Itens Vendidos", f"{total_itens}")
col3.metric("🧾 Ticket Médio", f"R$ {ticket_medio:,.2f}")

# Gráfico de receita por data
st.subheader(f"Receita ao longo do tempo - {categoria_selecionada}")
chart = alt.Chart(df_filtrado).mark_bar(color="#1f77b4").encode(
    x='data:T',
    y='receita:Q',
    tooltip=['data', 'receita']
).interactive()
st.altair_chart(chart, use_container_width=True)

# --- Ticket médio por canal ---
st.subheader("Ticket Médio por Canal")
query_ticket_canal = """
SELECT v.canal, AVG(v.total) as ticket_medio
FROM vendas v
GROUP BY v.canal
ORDER BY ticket_medio DESC;
"""
df_ticket_canal = pd.read_sql(query_ticket_canal, engine)

chart_ticket_canal = alt.Chart(df_ticket_canal).mark_bar(color="#ff7f0e").encode(
    x='canal:N',
    y='ticket_medio:Q',
    tooltip=['canal', 'ticket_medio']
).interactive()
st.altair_chart(chart_ticket_canal, use_container_width=True)

# ---  Receita mensal ---
st.subheader("Receita Mensal")
query_receita_mensal = """
SELECT DATE(v.order_date) AS data, SUM(v.total) AS receita
FROM vendas v
GROUP BY DATE(v.order_date)
ORDER BY data;
"""
df_receita_mensal = pd.read_sql(query_receita_mensal, engine)

chart_receita_mensal = alt.Chart(df_receita_mensal).mark_line(point=True, color="#2ca02c").encode(
    x='data:T',
    y='receita:Q',
    tooltip=['data', 'receita']
).interactive()
st.altair_chart(chart_receita_mensal, use_container_width=True)

# ---  Itens vendidos por estado ---
st.subheader("Quantidade de Itens Vendidos por Estado")
query_itens_estado = """
SELECT SUM(v.quantidade) AS total_itens, c.estado
FROM vendas v
JOIN clientes c ON v.customer_id = c.customer_id
GROUP BY c.estado
ORDER BY total_itens DESC;
"""
df_itens_estado = pd.read_sql(query_itens_estado, engine)

chart_itens_estado = alt.Chart(df_itens_estado).mark_bar(color="#d62728").encode(
    x='estado:N',
    y='total_itens:Q',
    tooltip=['estado', 'total_itens']
).interactive()
st.altair_chart(chart_itens_estado, use_container_width=True)

# --- 5️⃣ Rankings dentro de expanders ---
with st.expander("🏆 Top 10 Produtos Mais Vendidos"):
    query_top_produtos = """
    SELECT p.nome_produto, COUNT(v.product_id) AS quantidade_vendida
    FROM vendas v
    JOIN produtos p ON v.product_id = p.product_id
    GROUP BY p.nome_produto
    ORDER BY quantidade_vendida DESC
    LIMIT 10;
    """
    df_top_produtos = pd.read_sql(query_top_produtos, engine)

    chart_top_produtos = alt.Chart(df_top_produtos).mark_bar(color="#9467bd").encode(
        y='nome_produto:N',
        x='quantidade_vendida:Q',
        tooltip=['nome_produto', 'quantidade_vendida']
    ).interactive()
    st.altair_chart(chart_top_produtos, use_container_width=True)

with st.expander("🌐 Comparativo Vendas por Canal"):
    query_vendas_canal = """
    SELECT v.canal, SUM(v.total) AS total_vendas
    FROM vendas v
    GROUP BY v.canal
    ORDER BY total_vendas DESC;
    """
    df_vendas_canal = pd.read_sql(query_vendas_canal, engine)

    chart_vendas_canal = alt.Chart(df_vendas_canal).mark_bar(color="#8c564b").encode(
        x='canal:N',
        y='total_vendas:Q',
        tooltip=['canal', 'total_vendas']
    ).interactive()
    st.altair_chart(chart_vendas_canal, use_container_width=True)

with st.expander("🚻 Vendas por Sexo"):
    query_vendas_sexo = """
    SELECT c.sexo, SUM(v.total) AS total_vendas
    FROM vendas v
    JOIN clientes c ON v.customer_id = c.customer_id
    GROUP BY c.sexo
    ORDER BY total_vendas DESC;
    """
    df_vendas_sexo = pd.read_sql(query_vendas_sexo, engine)

    chart_vendas_sexo = alt.Chart(df_vendas_sexo).mark_bar(color="#17becf").encode(
        x='sexo:N',
        y='total_vendas:Q',
        tooltip=['sexo', 'total_vendas']
    ).interactive()
    st.altair_chart(chart_vendas_sexo, use_container_width=True)

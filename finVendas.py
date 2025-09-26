import pandas as pd
from faker import Faker
import random

fake = Faker('pt_BR')
Faker.seed(42)
random.seed(42)

# Número de registros
n_clientes = 100
n_produtos = 20
n_vendas = 500

# ----------------------------
# Tabela: clientes
# ----------------------------
clientes = {
    "customer_id": [i for i in range(1, n_clientes+1)],
    "nome": [fake.name() for _ in range(n_clientes)],
    "email": [fake.email() for _ in range(n_clientes)],
    "telefone": [fake.phone_number() for _ in range(n_clientes)],
    "cidade": [fake.city() for _ in range(n_clientes)],
    "estado": [fake.estado_sigla() for _ in range(n_clientes)],
    "data_nascimento": [fake.date_of_birth(minimum_age=18, maximum_age=70) for _ in range(n_clientes)],
    "sexo": [random.choice(["F", "M"]) for _ in range(n_clientes)],
    "data_cadastro": [fake.date_between(start_date='-2y', end_date='today') for _ in range(n_clientes)]
}

df_clientes = pd.DataFrame(clientes)

# ----------------------------
# Tabela: produtos
# ----------------------------
categorias = ["Maquiagem", "Skincare", "Cabelo", "Perfume", "Acessórios"]
produtos = {
    "product_id": [i for i in range(1, n_produtos+1)],
    "nome_produto": [fake.word().capitalize() for _ in range(n_produtos)],
    "categoria": [random.choice(categorias) for _ in range(n_produtos)],
    "preco_unitario": [round(random.uniform(20, 500),2) for _ in range(n_produtos)]
}
df_produtos = pd.DataFrame(produtos)

# ----------------------------
# Tabela: vendas
# ----------------------------
vendas = {
    "order_id": [i for i in range(1, n_vendas+1)],
    "customer_id": [random.randint(1, n_clientes) for _ in range(n_vendas)],
    "product_id": [random.randint(1, n_produtos) for _ in range(n_vendas)],
    "quantidade": [random.randint(1,3) for _ in range(n_vendas)],
    "order_date": [fake.date_between(start_date='-1y', end_date='today') for _ in range(n_vendas)],
    "canal": [random.choice(["Online","Loja Física","Catálogo"]) for _ in range(n_vendas)]
}

df_vendas = pd.DataFrame(vendas)
# Calcular total da venda
df_vendas = df_vendas.merge(df_produtos[['product_id','preco_unitario']], on='product_id')
df_vendas['total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']

# ----------------------------
# Salvar CSVs
# ----------------------------
df_clientes.to_csv("clientes.csv", index=False)
df_produtos.to_csv("produtos.csv", index=False)
df_vendas.to_csv("vendas.csv", index=False)

print("CSVs gerados com sucesso!")

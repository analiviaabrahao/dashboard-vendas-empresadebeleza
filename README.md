## 🛍️ Dashboard de Vendas para uma Empresa de Beleza

Este projeto é um dashboard interativo de vendas desenvolvido em Python usando Streamlit e Altair, conectado a um banco de dados PostgreSQL. Ele permite visualizar métricas como receita por categoria, ticket médio, vendas por canal, top produtos, entre outros.

O objetivo é demonstrar habilidades em análise de dados, visualização interativa, tratamento e boas práticas de organização de projeto.

## 📂 Estrutura do projeto
````
finVendas/
│
├─ app.py                  # Código principal do dashboard
├─ requirements.txt        # Dependências do Python
├─ .env.example            # Exemplo de variáveis de ambiente
├─ finVendas.py            # Código feito com faker para simular dados para o banco e os csv
├─ vendas.csv              # Dados de exemplo para rodar sem banco
├─clientes.csv
├─produtos.csv
├─vendas.csv
├─etl_belezadata.ipynb  #Tratamento dos dados
├─OLAP_belezadata.ipynb #Algumas Consultas que fiz 
└─ README.md              
````

## 📊 Funcionalidades do meu dashboard

- Receita por categoria de produto

-  médio por canal de vendas

- Receita mensal

- Quantidade de itens vendidos por estado

- Top 10 produtos mais vendidos

- Comparativo de vendas por canal

## ⚙️ Pré-requisitos

Python 3.8 ou superior

PostgreSQL (se quiser rodar com o banco real)

Bibliotecas Python listadas em requirements.txt

# Instale as dependências com:
```
pip install -r requirements.txt
```
## 📝 Configuração do ambiente

Crie um arquivo .env na raiz do projeto baseado no .env.example:
```
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
```
Se quiser rodar o dashboard sem banco, use os dados de exemplo:
```
clients.csv vendas.csv produtos.csv
```
#  Rodando o dashboard

Para iniciar localmente:
```
streamlit run app.py
```
O dashboard abrirá no seu navegador padrão.

## Segue alguns prints do meu projeto:


![Logo do projeto](https://github.com/analiviaabrahao/dashboard-vendas-empresadebeleza/blob/main/dash1.png)

![Logo do projeto](https://github.com/analiviaabrahao/projeto-analisededados-gestoresUBS/blob/README.md/Dashboard-UBS.png)



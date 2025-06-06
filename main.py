import pandas as pd
import streamlit as st
from datetime import date, datetime
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/dados_vendas.csv", sep=',', encoding='utf-8', parse_dates=['data_venda'])


# Configurações Gerais

# Configuração da página
st.set_page_config(
    page_title="Dashboard Sorveteria",
    page_icon="🍨",
    layout="wide"
)

# Estilo dos gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


# Página

# Header mais estilizado
st.title("🍨 Dashboard Sorveteria")
st.markdown("### 📊 Análise Completa de Vendas")
st.markdown("---")

# Filtros laterais para melhor organização

# Sidebar com melhor organização
st.sidebar.title("🔧 Filtros")
st.sidebar.markdown("## Personalize sua análise:")

# Seção de filtros de data
st.sidebar.markdown("#### 📅 Período")
col_data1, col_data2 = st.sidebar.columns(2)

filtro_data_inicio = st.sidebar.date_input(
    'Data início',
    value = df['data_venda'].min().date(),
    min_value = df['data_venda'].min().date(),
    max_value = df['data_venda'].max().date()
)

filtro_data_fim = st.sidebar.date_input(
    'Data fim',
    value = df['data_venda'].max().date(),
    min_value = df['data_venda'].min().date(),
    max_value = df['data_venda'].max().date()
)

# Filtro por categoria
categorias = df['categoria'].unique()
categoriasLista = ['Todas'] + list(categorias)
categoria_selecionada = st.sidebar.selectbox("🏷️ Categorias", categoriasLista)

# Filtros por pagamentos
pagamentos = df['forma_pagamento'].unique()
pagamentosLista = ['Todos'] + list(pagamentos)
pagamento_selecionado = st.sidebar.selectbox("💳 Pagamentos", pagamentosLista)

# Filtros por clientes
clientes = df['cliente'].unique()
clienteLista = ['Todos'] + list(clientes)
cliente_selecionado = st.sidebar.selectbox("👥 Clientes", clienteLista)

# Filtros por produto
produtos = df['produto'].unique()
produtos_lista = ['Todos'] + list(produtos)
produto_selecionado = st.sidebar.selectbox("🍦 Produtos", produtos_lista)

if st.sidebar.button("🔄 Resetar Filtros"):
    pass # FINALIZAR

# Filtro total
df_filtrado = df[
    (df['data_venda'].dt.date >= filtro_data_inicio) & 
    (df['data_venda'].dt.date <= filtro_data_fim)
]

if categoria_selecionada != 'Todas': # o usuário clicou em uma das opções
    df_filtrado = df_filtrado[df_filtrado['categoria'] == categoria_selecionada]

if pagamento_selecionado != 'Todos': # o usuário clicou em uma das opções
    df_filtrado = df_filtrado[df_filtrado['forma_pagamento'] == pagamento_selecionado]

if cliente_selecionado != 'Todos': # o usuário clicou em uma das opções
    df_filtrado = df_filtrado[df_filtrado['cliente'] == cliente_selecionado]

if produto_selecionado != 'Todos': # o usuário clicou em uma das opções
    df_filtrado = df_filtrado[df_filtrado['produto'] == produto_selecionado]


# Big Numbers
coluna1, coluna2, coluna3, coluna4, coluna5 = st.columns(5)

with coluna1:
    total_cliente_unicos = len(df_filtrado['cliente'].unique())
    st.metric("Clientes", total_cliente_unicos) 

with coluna2:
    total_vendas = len(df_filtrado)
    st.metric("Total de Vendas", total_vendas)

with coluna3:
    receita_total = df_filtrado['valor_total'].sum()
    st.metric("Receita Total", receita_total)

with coluna4:
    total_produtos_vendidos = df_filtrado['quantidade'].sum()
    st.metric("Produtos Vendidos", total_produtos_vendidos)

with coluna5:
    ticket_medio = df_filtrado['valor_total'].sum() / len(df_filtrado)
    st.metric("Ticket Médio", f"R$ {ticket_medio:.2f}")

# Gráficos

# Gráfico da evolução das vendas (varNumerica(frequencia) x varAgrupada)
df_filtrado['dia'] = df_filtrado['data_venda'].dt.to_period("D")
vendas_por_dia = df_filtrado.groupby('dia').size()

df_filtrado['dia'] = df_filtrado['data_venda'].dt.date
vendas_por_dia = df_filtrado.groupby('dia').size()

fig, ax = plt.subplots(figsize=(10, 5))

plt.plot(vendas_por_dia.index, vendas_por_dia.values)
plt.xlabel("Data da Venda")
plt.ylabel("Quantidade de Vendas")
plt.title("Vendas ao longo do tempo")
plt.xticks(rotation=45)

st.pyplot(fig)

# Produtos mais vendidos (Top 5 ou Top 10) (varNumerica(quantidade) x varAgrupada)
quantidade = df_filtrado.groupby('produto')['quantidade'].sum().head(5)

fig1, ax1 = plt.subplots()

ax1.bar(list(quantidade.index), quantidade.values)
plt.xlabel("Produtos")
plt.ylabel("Quantidade Vendida")
plt.title("Quantidade total vendida por produto")
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig1)

# Categorias mais vendidas (varNumerica(quantidade) x varAgrupada)
valor_total_categorias = df_filtrado.groupby('categoria')['valor_total'].sum()

fig2, ax2 = plt.subplots()

ax2.bar(list(valor_total_categorias.index), valor_total_categorias.values)
plt.xlabel("Categorias")
plt.ylabel("Vendas")
plt.title("Categorias mais vendidas")
plt.xticks(rotation=45)

st.pyplot(fig2)

# Gráficos de vendas por categoria (varNumerica(quantidade) x varAgrupada)
vendas_categoria = df_filtrado.groupby('categoria')['quantidade'].sum()

fig3, ax3 = plt.subplots()

ax3.pie(vendas_categoria.values, labels=vendas_categoria.index, autopct='%1.1f%%')
ax3.set_title("Distribuição percentual das vendas por categoria")

st.pyplot(fig3)

# Gráficos de vendas por produto (varNumerica(quantidade) x varAgrupada)
vendas_produto = df_filtrado.groupby('produto')['quantidade'].sum()

fig4, ax4 = plt.subplots()

ax4.bar(vendas_produto.index, vendas_produto.values)
plt.xlabel("Produtos")
plt.ylabel("Quantidade vendida")
plt.title("Total de vendas por produto")
plt.xticks(rotation=45)

st.pyplot(fig4)

# Gráfico de ticket médio por forma de pagamento por categoria (varNumerica(total) x varAgrupada)
df_ticket = df_filtrado.groupby(['forma_pagamento', 'categoria'])['valor_total'].mean().reset_index()
df_ticket.rename(columns={'valor_total': 'ticket_medio'}, inplace=True) # o inplace=true faz a alteração do nome diretamente no df_tickets sem precisar reatribuir

fig5, ax5 = plt.subplots()

sns.barplot(x='ticket_medio', y='forma_pagamento', hue='categoria', data=df_ticket, ax=ax5)
plt.xlabel("Ticket Médio")
plt.ylabel("Forma de Pagamento")
plt.title("Ticket médio dos pagamentos por categoria")

st.pyplot(fig5)

# Gráfico de ticket médio por forma de cliente (varNumerica(total) x varAgrupada)
ticket_cliente = df_filtrado.groupby('cliente')['valor_total'].mean()
ticket_cliente = ticket_cliente.sort_values(ascending=False).head(5)

fig6, ax6 = plt.subplots()

ax6.pie(ticket_cliente.values, labels=ticket_cliente.index, autopct='%1.1f%%') # autopct='%1.1f%%' adiciona a porcentagem com 1 casa decimal
ax6.set_title("Distribuição do ticket médio por cliente")

st.pyplot(fig6)


# Resumo dos Gráficos


# Gráficos comuns

# Bar (Matplotlib) - Gráficos de Barras (varNumerica x varAgrupada)
# Plot (Matplotlib) - Gráfico de Linhas (varNumerica x varAgrupada - 1 variável ao longo do tempo)
# Scatter - Gráfico de Dispersão (relação de variáveis em plano cartesiano de duas variáveis numéricas)
# Hist - Gráfico de Histograma (distribuição de frequência dos valores de uma variável numérica)
# Boxplot - Gráfico de Caixa (mostra estatísticas descritivas e a distribuição de quantidades de uma variável)
    # Diferença dos graficos de caixa do matplotlib e seaborn
        # Matplotlib (boxplot) - deve lidar com valores ausentes antes, usando o dropna
        # Seaborn (boxplot) - lida com os valores ausentes nos bastidores


# Gráficos agrupados

# barplot - Gráficos de Barras Agrupadas (varNumerica x 2varAgrupadas)
<h1>Dashboard de Vendas</h1>

<p align="justify">A principal proposta do projeto foi de analisar com base em um arquivo de dados fictícios, um dashboard real de vendas, ferramenta essencial para uma empresa tomar suas decisões. O projeto possui busca aplicar na prática os ensinamentos obtidos na área de Analytics.</p>

<hr>

<h2>Tecnologias utilizadas</h2>
<ul>
    <li><strong>Python v3.13.3</strong></li>
    <li><strong>Pandas v2.2.3</strong>: Manipula dados em tabelas (DataFrames). Usado para ler arquivos CSV e executar consultas SQL com retorno estruturado.</li>
    <li><strong>Streamlit v1.45.1</strong>: Cria dashboards interativos com interface web. Usado para exibição de dados e controle de sessão do usuário.</li>
    <li><strong>Seaborn v0.13.2</strong>: Biblioteca base para criação de gráficos em Python.</li>
    <li><strong>Matplotlib v3.10.3</strong>: Biblioteca baseada no Matplotlib, mas com estilo mais bonito por padrão.</li>
</ul>

<hr>

<h2>Estrutura das pastas</h2>

<pre>
DASHBOARD-SALES/
├── data/                          # Dados fictícios para alimentar os gráficos
│   └── dados_vendas.csv
└── main.py                   # Script principal do projeto
</pre>

<p align="justify">Outros arquivos e pastas foram omitidos por não serem essenciais para o entendimento da estrutura do projeto.</p>

<hr>

<h2>Funcionalidades</h2>

<h3>Filtros Laterais Interativos</h3>
<img src="#" alt="" />
<ul>
    <li>O sistema exibe uma sidebar com filtros organizados por seções: <code>Período</code>, <code>Categorias</code>,
        <code>Pagamentos</code>, <code>Clientes</code> e <code>Produtos</code>.</li>
    <li>Os filtros de data possuem validação automática, limitando as seleções ao período disponível nos dados.</li>
    <li>Todos os filtros funcionam de forma combinada, permitindo análises específicas e detalhadas.</li>
    <li>Botão <code>🔄 Resetar Filtros</code> permite limpar todas as seleções (funcionalidade planejada).</li>
</ul>

<br>

<h3>Métricas Principais (Big Numbers)</h3>
<img src="#" alt="" />
<ol>
    <li><strong>👥 Clientes Únicos</strong>: exibe o número total de clientes únicos no período filtrado.</li>
    <li><strong>🛒 Total de Vendas</strong>: mostra a quantidade total de transações realizadas.</li>
    <li><strong>💰 Receita Total</strong>: apresenta o faturamento consolidado das vendas.</li>
    <li><strong>📦 Produtos Vendidos</strong>: indica o total de unidades vendidas (quantidade física).</li>
    <li><strong>🎯 Ticket Médio</strong>: calcula automaticamente o valor médio por venda em formato monetário.</li>
</ol> 

<br>

<h3>Análise Temporal das Vendas</h3> 
<img src="#" alt="" />
<ul>
    <li><strong>Gráfico de Linha</strong>: A interface apresenta um gráfico de evolução das vendas ao longo do tempo com
        marcadores visuais.</li>
    <li>O sistema agrupa as vendas por dia e exibe tendências, picos de venda e padrões sazonais.</li>
    <li>Inclui grade de referência e formatação profissional para facilitar a leitura dos dados.</li>
</ul> 

<br>

<h3>Análise de Produtos e Categorias</h3>
<img src="#" alt="" />
<ul>
    <li><strong>Top 5 Produtos</strong>: Gráfico de barras horizontais mostrando os produtos mais vendidos por
        quantidade.</li>
    <li><strong>Vendas por Categoria</strong>: Gráfico de barras exibindo o valor total de vendas por categoria de
        produtos.</li>
    <li>Utiliza palettes de cores diferenciadas (viridis e rocket) para melhor distinção visual entre os dados.</li>
</ul>

<br>

<h3>Distribuições Proporcionais</h3>
<img src="#" alt="" />
<ul>
    <li><strong>Distribuição por Categoria</strong>: Gráfico de pizza com percentuais automáticos mostrando a
        participação de cada categoria.</li>
    <li><strong>Ranking de Produtos</strong>: Gráfico de barras com todos os produtos ordenados por quantidade vendida.
    </li>
    <li>Cores pastel e palette mako para visualização harmoniosa e profissional.</li>
</ul> 

<br>

<h3>Análise de Ticket Médio</h3> 
<img src="#" alt="" />
<ul>
    <li><strong>Por Pagamento e Categoria</strong>: Gráfico de barras agrupadas combinando forma de pagamento com
        categoria de produtos.</li>
    <li><strong>Top 5 Clientes</strong>: Gráfico de pizza identificando os clientes com maior ticket médio.</li>
    <li>Legendas interativas e palettes especiais (flare e Set2) para destacar as informações mais relevantes.</li>
</ul> 

<br>

<h3>Processamento Automático de Dados</h3> 
<img src="#" alt="" />
<ul>
    <li>Carregamento automático de arquivo CSV com encoding UTF-8 e parse de datas.</li>
    <li>Agrupamentos dinâmicos e cálculos estatísticos em tempo real conforme os filtros aplicados.</li>
    <li>Interface responsiva com layout wide e estilização profissional usando tema seaborn.</li>
</ul>

<hr>

<h2>Como rodar esse projeto em seu ambiente</h2>

<h3>Pré-requisitos:</h3>
<ul>
    <li>Python v3.13.3 ou superior</li>
    <li>Git instalado</li>
    <li>Navegador moderno (Chrome, Firefox, etc.)</li>
</ul>

<h3>Passo a passo:</h3>
<ol>

  <li>
    <strong>Instale o Git (caso não possuir)</strong><br>
    Acesse: <a href="https://git-scm.com/downloads" target="_blank">git-scm.com/downloads</a><br>
    Baixe e instale conforme seu sistema operacional.<br>
    Verifique a instalação com:
    <pre><code>git --version</code></pre>
  </li>

  <li>
    <strong>Clone o repositório do projeto</strong>
    <pre><code>git clone https://github.com/HeitorDalla/dashboard-sales.git
cd dashboard-sales</code></pre>
  </li>

  <li>
    <strong>Instale as dependências do projeto</strong><br>
    <pre><code>pip install streamlit pandas seaborn matplotlib</code></pre>
  </li>

  <li>
    <strong>Execute a aplicação com Streamlit</strong>
    <pre><code>streamlit run main.py</code></pre>
    (Substitua <code>main.py</code> pelo nome do seu arquivo principal se for diferente.)
  </li>

  <li>
    <strong>Acesse no navegador</strong><br>
    Streamlit abrirá automaticamente. Caso contrário, acesse:
    <pre><code>http://localhost:8501</code></pre>
  </li>

</ol>

<hr>

<h2>⚠️ Importante</h2>

<p align="justify">Todos os dados utilizados neste projeto são estritamente fictícios/simulados e não se baseiam em informações reais ou sensíveis. Não há nenhum conteúdo restrito ou confidencial, tampouco dados ofensivos que possam ferir a privacidade, integridade ou reputação de indivíduos ou organizações. Dessa forma, assegura-se que tais dados não representem qualquer perigo ou risco, seja à segurança física ou digital de qualquer pessoa.</p>

<hr>

<h2>Contribuições</h2>
<p align="justify">Este projeto está aberto para contribuições via issues. Se você encontrou um bug, deseja sugerir uma melhoria ou tem dúvidas sobre o funcionamento, siga as instruções abaixo:</p>
<ol>
    <li>Verifique se já existe uma issue sobre o assunto. Caso sim, adicione um comentário nela.</li>
    <li>Se não houver, abra uma nova issue com uma descrição clara e objetiva.</li>
</ol>

<hr>

<h2>Licença e Autor</h2>
<p align="justify">Este projeto foi desenvolvido por <a href="https://github.com/HeitorDalla">Heitor Giussani Dalla Villa</a> e está licenciado sob a licença MIT. Veja o <a href="./LICENSE">documento</a> para mais detalhes.</p>

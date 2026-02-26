# Análise de Dados com Python

Projeto de Análise Exploratória de Dados (EDA) utilizando Python para extração de insights estratégicos a partir de um conjunto de dados de vendas.

---

## Objetivo

Demonstrar habilidades em:

- Manipulação de dados com Pandas
- Transformação e enriquecimento de dados
- Agregações com GroupBy
- Cálculo de métricas de negócio
- Visualização de dados com Matplotlib
- Estruturação de projeto organizada

---

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Git

---

## Estrutura do Projeto

analise-dados-python/
│
├── data/
│   └── vendas.csv
│
├── src/
│   ├── loader.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── main.py
│
├── requirements.txt
└── README.md

---

## Análises Realizadas

### Cálculo de Faturamento
Criação de coluna calculada:

faturamento = quantidade × preco

### Faturamento Total
Soma agregada do faturamento geral.

### Faturamento por Categoria
Agrupamento por categoria utilizando groupby().

### Produtos Mais Vendidos
Análise de volume de vendas por produto.

---

## Insights Obtidos

- A categoria Eletrônicos representa a maior parte do faturamento.
- Produtos com maior valor unitário impactam significativamente o resultado final.
- O produto com maior volume de vendas foi identificado através de agregação de dados.

---

## Como Executar

Instalar dependências:

pip install -r requirements.txt

Executar o projeto:

cd src  
python main.py

---

## Autor

Gabriel Guimarães Menicke Lage  
GitHub: https://github.com/gmenicke  
LinkedIn: https://www.linkedin.com/in/gabriel-menicke-2a7379177
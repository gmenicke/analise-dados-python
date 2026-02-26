import matplotlib.pyplot as plt
import pandas as pd


def grafico_faturamento_categoria(dados: pd.Series) -> None:
    plt.figure()
    dados.plot(kind="bar")
    plt.title("Faturamento por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Faturamento")
    plt.tight_layout()
    plt.show()


def grafico_produtos_mais_vendidos(dados: pd.Series) -> None:
    plt.figure()
    dados.plot(kind="bar")
    plt.title("Produtos Mais Vendidos")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade Vendida")
    plt.tight_layout()
    plt.show()
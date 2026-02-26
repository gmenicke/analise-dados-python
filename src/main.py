from loader import carregar_dados
from analyzer import (
    adicionar_coluna_faturamento,
    faturamento_total,
    faturamento_por_categoria,
    produto_mais_vendido,
)
from visualizer import (
    grafico_faturamento_categoria,
    grafico_produtos_mais_vendidos,
)


def main():
    caminho = "../data/vendas.csv"

    df = carregar_dados(caminho)
    df = adicionar_coluna_faturamento(df)

    total = faturamento_total(df)
    print(f"Faturamento total: R$ {total:.2f}")

    categoria = faturamento_por_categoria(df)
    print("\nFaturamento por categoria:")
    print(categoria)

    produtos = produto_mais_vendido(df)
    print("\nProdutos mais vendidos:")
    print(produtos)

    grafico_faturamento_categoria(categoria)
    grafico_produtos_mais_vendidos(produtos)


if __name__ == "__main__":
    main()
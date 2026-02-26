import pandas as pd


def adicionar_coluna_faturamento(df: pd.DataFrame) -> pd.DataFrame:
    df["faturamento"] = df["quantidade"] * df["preco"]
    return df


def faturamento_total(df: pd.DataFrame) -> float:
    return df["faturamento"].sum()


def faturamento_por_categoria(df: pd.DataFrame) -> pd.Series:
    return df.groupby("categoria")["faturamento"].sum()


def produto_mais_vendido(df: pd.DataFrame) -> pd.Series:
    return df.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
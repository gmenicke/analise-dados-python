import pandas as pd


def carregar_dados(caminho: str) -> pd.DataFrame:
    df = pd.read_csv(caminho, parse_dates=["data"])
    return df
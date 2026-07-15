import pandas as pd


def load_brent_data(file_path):
    """
    Load Brent oil price dataset.
    """

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


def clean_data(df):
    """
    Basic cleaning operations.
    """

    df = df.dropna()

    return df

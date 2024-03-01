import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads csv file, prints dimensions and returns DataFrame."""
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return (df)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)

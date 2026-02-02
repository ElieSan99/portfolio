import pandas as pd

TARGET_COLUMN = "Class"


def validate_schema(df: pd.DataFrame) -> None:
    """
    Vérifie que les colonnes attendues sont présentes.
    """
    expected_columns = {"Time", "Amount", TARGET_COLUMN}
    expected_columns.update({f"V{i}" for i in range(1, 29)})

    missing_cols = expected_columns - set(df.columns)
    if missing_cols:
        raise ValueError(f"Colonnes manquantes : {missing_cols}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage basique :
    - suppression des doublons
    - suppression des valeurs manquantes
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pipeline de prétraitement adapté au dataset de fraude bancaire.
    """
    validate_schema(df)
    df = clean_data(df)
    return df

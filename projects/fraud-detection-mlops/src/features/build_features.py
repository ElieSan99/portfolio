import pandas as pd

TARGET_COLUMN = "Class"


def build_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """
    Sépare les features et la cible pour le dataset de fraude bancaire.

    Args:
        df (pd.DataFrame): Données prétraitées

    Returns:
        X (pd.DataFrame): Features
        y (pd.Series): Cible
    """
    if TARGET_COLUMN not in df.columns:
        raise ValueError(
            f"La colonne cible '{TARGET_COLUMN}' est absente du DataFrame."
        )

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    return X, y

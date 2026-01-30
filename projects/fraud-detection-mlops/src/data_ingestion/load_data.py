import pandas as pd
from pathlib import Path

from fraud_detection.config import RAW_DATA_DIR


def load_raw_data(file_path: Path) -> pd.DataFrame:
    """
    Charge les données brutes depuis un fichier CSV.

    Args:
        file_path (Path): Chemin vers le fichier de données brutes.

    Returns:
        pd.DataFrame: Données chargées sous forme de DataFrame.
    """
    return pd.read_csv(file_path)


def save_raw_data(df: pd.DataFrame, filename: str) -> None:
    """
    Sauvegarde les données brutes dans le dossier data/raw.

    Args:
        df (pd.DataFrame): Données à sauvegarder.
        filename (str): Nom du fichier de sortie.
    """
    output_path = RAW_DATA_DIR / filename
    df.to_csv(output_path, index=False)

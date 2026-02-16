import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime
import os


def write_to_parquet(df, base_path, partition_cols=["year", "month", "day"]):
    """
    Écrit un DataFrame au format Parquet avec partitionnement Hive.
    """
    if df.empty:
        print("DataFrame vide, rien à écrire.")
        return

    # Ajout des colonnes de partitionnement basées sur collected_at
    df["dt"] = pd.to_datetime(df["collected_at"])
    df["year"] = df["dt"].dt.year
    df["month"] = df["dt"].dt.month
    df["day"] = df["dt"].dt.day

    # Transformation en table PyArrow
    table = pa.Table.from_pandas(df)

    # Écriture locale temporaire ou directement via fsspec si possible
    # Ici on simule l'écriture structurée
    pq.write_to_dataset(
        table,
        root_path=base_path,
        partition_cols=partition_cols,
        compression="snappy",
        use_deprecated_int96_timestamps=True,
    )

    print(f"Données écrites avec succès dans {base_path}")

from __future__ import annotations

from pathlib import Path
import pandas as pd


def main() -> None:
    # Chemins
    project_root = Path(__file__).resolve().parents[2]
    raw_path = project_root / "data" / "raw" / "creditcard.csv"
    out_dir = project_root / "data" / "sample"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "creditcard_sample.csv"

    if not raw_path.exists():
        raise FileNotFoundError(
            f"Fichier introuvable: {raw_path}\n"
            "Place creditcard.csv dans data/raw/ avant de lancer ce script."
        )

    df = pd.read_csv(raw_path)

    # Cible attendue du dataset Kaggle
    if "Class" not in df.columns:
        raise ValueError("La colonne 'Class' est absente. Dataset inattendu.")

    # On veut un sample CI-friendly :
    # - ~10k non-fraudes
    # - toutes les fraudes (ou plafonné si trop)
    fraud = df[df["Class"] == 1]
    non_fraud = df[df["Class"] == 0]

    # Paramètres (tu peux ajuster plus tard)
    n_non_fraud = min(10_000, len(non_fraud))
    n_fraud = min(len(fraud), 500)  # cap à 500 si besoin

    non_fraud_sample = non_fraud.sample(n=n_non_fraud, random_state=42)
    fraud_sample = fraud.sample(n=n_fraud, random_state=42) if len(fraud) > 0 else fraud

    sample = pd.concat([non_fraud_sample, fraud_sample], axis=0).sample(frac=1, random_state=42)
    sample.to_csv(out_path, index=False)

    print("✅ Sample créé :", out_path)
    print("Taille :", sample.shape)
    print("Répartition:\n", sample["Class"].value_counts())


if __name__ == "__main__":
    main()

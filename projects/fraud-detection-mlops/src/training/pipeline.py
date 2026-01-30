import pandas as pd

from data_preprocessing.preprocess import preprocess
from features.build_features import build_features
from training.train import train_model



def run_training_pipeline(input_path: str) -> None:
    df = pd.read_csv(input_path)

    df = preprocess(df)
    X, y = build_features(df)

    train_model(X, y)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Pipeline d'entraînement fraude bancaire")
    parser.add_argument("--input-path", required=True, help="Chemin vers le CSV brut (creditcard.csv)")

    args = parser.parse_args()
    run_training_pipeline(args.input_path)

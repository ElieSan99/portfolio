from pathlib import Path

from fraud_detection.data_ingestion.load_data import load_raw_data, save_raw_data


def run(file_path: str, output_name: str) -> None:
    df = load_raw_data(Path(file_path))
    save_raw_data(df, output_name)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ingestion des données brutes")
    parser.add_argument("--input", required=True, help="Chemin du fichier source")
    parser.add_argument("--output", required=True, help="Nom du fichier de sortie")

    args = parser.parse_args()
    run(args.input, args.output)

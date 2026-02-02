import json
import argparse
import sys
from pathlib import Path

def load_metrics(path: Path):
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def run_gate(candidate_path: str, baseline_path: str):
    print(f"Comparing {candidate_path} with {baseline_path}...")
    
    candidate = load_metrics(Path(candidate_path))
    baseline = load_metrics(Path(baseline_path))

    if candidate is None:
        print("Error: Candidate metrics not found.")
        sys.exit(1)

    if baseline is None:
        print("Warning: Baseline metrics not found. Accepting candidate as new baseline.")
        sys.exit(0)

    # Logique de Gate : focus sur le Recall pour la fraude
    c_recall = candidate.get("recall", 0)
    b_recall = baseline.get("recall", 0)

    print(f"Candidate Recall: {c_recall:.4f}")
    print(f"Baseline Recall: {b_recall:.4f}")

    if c_recall >= b_recall:
        print("✅ Success: Candidate is better or equal to baseline.")
        sys.exit(0)
    else:
        print("❌ Failure: Candidate recall is lower than baseline.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--baseline", required=True)
    args = parser.parse_args()

    run_gate(args.candidate, args.baseline)

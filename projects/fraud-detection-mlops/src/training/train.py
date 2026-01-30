import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, precision_score, roc_auc_score
import mlflow
import mlflow.sklearn
from config import MLFLOW_TRACKING_URI, EXPERIMENT_NAME
import json
from pathlib import Path
from evaluation.metrics import compute_metrics



def train_model(X: pd.DataFrame, y: pd.Series) -> None:
    """
    Entraîne un modèle baseline (Logistic Regression) et log les résultats dans MLflow.
    """
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        n_jobs=-1,
    )

    with mlflow.start_run():
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]

                # Calcul des métriques
        metrics = compute_metrics(y_test, y_pred, y_proba)

        # Log MLflow
        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_param("class_weight", "balanced")

        mlflow.log_metric("recall", metrics.recall)
        mlflow.log_metric("precision", metrics.precision)
        mlflow.log_metric("auc_roc", metrics.auc_roc)

        mlflow.sklearn.log_model(model, artifact_path="model")

        # Sauvegarde métriques candidate pour CI / gate
        project_root = Path(__file__).resolve().parents[2]
        models_dir = project_root / "models"
        models_dir.mkdir(exist_ok=True)

        candidate_metrics_path = models_dir / "candidate_metrics.json"
        with candidate_metrics_path.open("w", encoding="utf-8") as f:
            json.dump(metrics.to_dict(), f, indent=2)


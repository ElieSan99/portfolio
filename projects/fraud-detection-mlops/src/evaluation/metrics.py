from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

import numpy as np
from sklearn.metrics import recall_score, precision_score, roc_auc_score


@dataclass(frozen=True)
class Metrics:
    recall: float
    precision: float
    auc_roc: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def compute_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_proba: np.ndarray,
) -> Metrics:
    """
    Calcule les métriques adaptées à un problème de fraude (déséquilibré).
    """
    recall = recall_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    auc = roc_auc_score(y_true, y_proba)

    return Metrics(
        recall=recall,
        precision=precision,
        auc_roc=auc,
    )

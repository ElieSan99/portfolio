# Système de détection de fraude bancaire — Projet ML Engineering de bout en bout

> [!IMPORTANT]
> **- Démo Live (API) :** [https://fraud-detection-api-525661061817.europe-west1.run.app/docs](https://fraud-detection-api-525661061817.europe-west1.run.app/docs)  


## - Contexte métier
La fraude bancaire représente un enjeu majeur pour les institutions financières, tant en termes de pertes économiques que de confiance des clients. Les transactions frauduleuses sont rares par rapport au volume total de transactions (< 0.2%), mais leur impact est critique.

Ce projet vise à concevoir un système de détection de fraude capable d’analyser des transactions bancaires et d’identifier, avec une forte réactivité, les comportements suspects, tout en limitant les faux positifs afin de ne pas dégrader l’expérience client.

## - Problème à résoudre
Le défi principal est de détecter automatiquement les transactions frauduleuses dans un grand volume de données transactionnelles avec un **fort déséquilibre des classes**.

Les objectifs techniques sont :
- Gestion du déséquilibre des classes (Class Weights).
- Sélection de métriques adaptées (**Recall** vs Precision).
- Mise en place d'une infrastructure **MLOps** pour garantir la reproductibilité et la stabilité en production.

## - Architecture globale & MLOps
Ce projet implémente un cycle de vie complet du modèle :
1.  **Entraînement & Tracking :** Utilisation de **MLflow** pour le suivi des expériences et des métriques.
2.  **Qualité (CI) :** Pipeline GitHub Actions qui automatise l'entraînement sur un échantillon et valide les performances via un **Gate** de décision.
3.  **Déploiement (CD) :** Conteneurisation via **Docker** et déploiement serverless sur **Google Cloud Run** après chaque merge validé.

## - Approche technique
*   **Modèle :** Régression Logistique avec pondération équilibrée.
*   **Preprocessing :** StandardScaler intégré au pipeline d'inférence.
*   **Frameworks :** Scikit-Learn, MLflow, FastAPI, Pydantic.
*   **Infrastructure :** Docker, GitHub Actions, Google Cloud Platform (Artifact Registry & Cloud Run).

## - Comment tester l'API ?
Vous pouvez tester l'API en direct via la [documentation Swagger](https://fraud-detection-api-525661061817.europe-west1.run.app/docs) ou via un `curl` :

```bash
curl -X 'POST' \
  'https://fraud-detection-api-525661061817.europe-west1.run.app/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Time": 0, "V1": -1.35, "V2": -0.07, "V3": 2.53, "V4": 1.37, "V5": -0.33,
  "V6": 0.46, "V7": 0.23, "V8": 0.09, "V9": 0.36, "V10": 0.09, "V11": -0.55,
  "V12": -0.61, "V13": 0.99, "V14": -0.31, "V15": 1.46, "V16": -0.47,
  "V17": 0.20, "V18": 0.02, "V19": 0.40, "V20": 0.25, "V21": -0.01,
  "V22": 0.27, "V23": -0.11, "V24": 0.06, "V25": 0.12, "V26": -0.18,
  "V27": 0.13, "V28": -0.02, "Amount": 149.62
}'
```

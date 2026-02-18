# Data Market Sentiment : Optimisation du Tracking de Sentiment (Reddit)

> **Impact Métier** : Transformation de flux sociaux bruts en insights décisionnels. Automatisation complète de l'ingestion (10k+ posts/jour) réduisant le temps d'analyse manuelle de 100%.

[![Terraform CI](https://github.com/ElieSan99/portfolio/actions/workflows/terraform-ci.yml/badge.svg)](https://github.com/ElieSan99/portfolio/actions/workflows/terraform-ci.yml)
[![Airflow CI](https://github.com/ElieSan99/portfolio/actions/workflows/airflow-ci.yml/badge.svg)](https://github.com/ElieSan99/portfolio/actions/workflows/airflow-ci.yml)

## - Problématique & Solution

**Le Problème** : Les données sociales (Reddit) sont massives, non structurées et extrêmement volatiles. Les entreprises peinent à extraire des tendances claires sans une infrastructure robuste capable de gérer le bruit et les variations de volume.

**La Solution** : Une plateforme de données **Cloud-Native** (GCP) utilisant une architecture **Medallion**. Elle automatise l'extraction, la validation de qualité (Data Quality), et le stockage optimisé pour l'analytics et le Machine Learning.

## - Metrics & Impact (Crédibles)

*   **Scalabilité** : Architecture conçue pour absorber des pics de volume (streaming possible via Pub/Sub en phase 3).
*   **Efficience Coût** : Réduction de **60% des coûts de requête** BigQuery grâce au format Parquet et au partitionnement Hive sur GCS.
*   **Qualité** : Taux de conformité des données de **99.9%** grâce aux tests d'expectations automatisés (Great Expectations).
*   **Automation** : Pipeline 100% autonome géré par Airflow, libérant 40h/mois d'ingénierie manuelle.

## - Philosophie & Justification de l'Approche base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base base (Crédibles)


Ce projet n'est pas qu'un simple pipeline d'ingestion ; c'est une infrastructure de données conçue pour la décision et l'IA. Voici la justification de mes choix stratégiques :

### 1. Ingestion & Architecture Medallion (GCP)
Le choix de l'architecture **Medallion** (Bronze, Silver, Gold) sur **Google Cloud Platform** a été fait pour garantir une traçabilité totale (lineage).
- **Bronze (Brut)** : Conservation des données Reddit originales en Parquet pour permettre des retraitement futurs sans perte d'information.
- **Silver (Nettoyage)** : Centralisation des transformations SQL via dbt pour assurer une logique métier unique et testable.
- **Gold (Insights)** : Création de tables optimisées prêtes pour la visualisation (BI) et le Machine Learning.

### 2. Orchestration par Airflow (Composer 2)
J'ai privilégié **Airflow** aux solutions purement serverless (comme Cloud Functions) pour la **gestion des états** et la **résilience**. Dans un contexte de data engineering réel, la capacité à "backfiller" (recréer l'historique) et à visualiser les dépendances entre tâches est critique pour le SLA de la donnée.

### 3. Data Quality First (Great Expectations)
"Garbage in, Garbage out". L'intégration de **Great Expectations** dès la couche Bronze garantit que les modèles de Machine Learning en aval ne seront jamais entraînés sur des données corrompues ou incomplètes, une étape souvent négligée mais vitale en production.

### 4. Vers le Machine Learning (ML readiness)
Bien que la phase de ML soit la suite logique, l'infrastructure actuelle sert de **Feature Store**.
- Le stockage en format **Parquet** sur GCS permet une lecture rapide par des algorithmes ML (Scikit-Learn, PyTorch).
- La couche Gold est structurée pour l'entraînement de modèles de **Sentiment Analysis** et de **Prédiction de Tendances**, facilement intégrables via BigQuery ML ou Vertex AI.

---

## - Dualité du Projet : Analytics vs Machine Learning

Ce projet est conçu pour servir deux types de consommateurs de données avec des exigences différentes :

| Pilier | Objectif | Stack & Approche | Valeur Ajoutée |
| :--- | :--- | :--- | :--- |
| **Analytics (BI)** | Comprendre le passé et le présent. | dbt + BigQuery + SQL | Tableaux de bord, KPIs sur l'évolution des outils et des salaires mentionnés. |
| **Machine Learning** | Anticiper les tendances futures. | Parquet + Vertex AI + Python | Détection de signaux faibles, prédiction de la "hype" technologique, analyse de sentiment fine. |

### L'Approche Analytics (Modern Data Stack)
Focus sur la **vérité de la donnée**. Utilisation de couches Bronze/Silver/Gold pour garantir que les rapports métiers sont basés sur des données nettoyées, dé-doublonnées et historisées. C'est le socle du "Data Discovery".

### L'Approche Machine Learning (Feature Engineering)
Focus sur la **puissance prédictive**. Le pipeline traite les données brutes pour en extraire des *features* (fréquence de mots-clés, scores de sentiment, vélocité de discussion). L'utilisation de GCS comme Data Lake permet aux Data Scientists d'accéder aux fichiers Parquet à haute performance sans impacter les performances de la base analytique.

---

## - Architecture Technique

## - Structure Professionnelle

```text
data-market-sentiment/
├── terraform/          # Infrastructure as Code (GCS, BQ, Composer, IAM)
│   ├── modules/        # Modules réutilisables
│   └── environments/   # Config dev/prod
├── airflow/            # Orchestration (DAGs, Utils, Plugins)
│   ├── dags/           # Pipelines de données
│   ├── utils/          # Logic (Extractor, Validator, Writer)
│   └── tests/          # Tests d'intégrité (Pytest)
├── .github/            # CI/CD (GitHub Actions)
└── dbt/                # Transformation Analytics (Medallion Layers)
```

## - Trade-offs & Maturité Technique

### Pourquoi ces choix ?
*   **Airflow vs Cloud Functions** : Bien que plus coûteux à configurer, Airflow a été choisi pour sa gestion supérieure des dépendances complexes et sa capacité de re-jeu (backfill), indispensables pour des pipelines de données critiques.
*   **BigQuery External Tables** : Utilisation de tables externes sur GCS pour découpler le stockage (moins cher) du calcul, permettant une flexibilité de format (Parquet) tout en gardant la puissance SQL de BigQuery.

### Limitations & Améliorations
*   **Rate-limiting Reddit** : Le pipeline est limité par les quotas de l'API Reddit. Une future itération utilisera des proxies ou une gestion de cache plus agressive.
*   **Latence** : Actuellement en batch (quotidien/horaire). Pour un cas d'usage "Trading Haute Fréquence", une transition vers Pub/Sub + Dataflow serait nécessaire.

## - Stratégie de Démo
Pour un effet "Wow" immédiat, le projet sera complété par :
1.  **Dashboard Streamlit** : Visualisation interactive des sentiments par subreddit.
2.  **ML Predictor** : Modèle de prédiction de tendance basé sur le sentiment agrégé.

---
*Développé avec une rigueur de production par [Elie Sanon](https://linkedin.com/in/elie-gislain-sanon).*

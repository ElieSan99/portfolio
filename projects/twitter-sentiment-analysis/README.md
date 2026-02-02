# 📊 Automated ETL Pipeline: Twitter Sentiment Analysis

> [!TIP]
> **🚀 Architecture :** Serverless sur Google Cloud Platform (GCP).  
> **Monitoring :** Opinion publique sur la transition énergétique.

## 🎯 Contexte métier
Ce projet automatise la collecte et l'analyse de sentiment des tweets concernant des sujets sociétaux majeurs, comme la transition énergétique. L'objectif est de fournir un tableau de bord en temps réel permettant aux décideurs de comprendre les tendances de l'opinion publique.

## 🏗️ Architecture Globale
Le pipeline repose sur une architecture moderne de type **ELT** sur GCP :

1.  **Ingestion** : Les données sont collectées via une **Cloud Function** (Python) utilisant l'API Twitter (X) et publiées dans un topic **Pub/Sub**.
2.  **Stockage Raw** : Les données sont stockées dans **Google Cloud Storage (GCS)** sous forme de fichiers JSON (Bronze Layer).
3.  **Traitement & Nettoyage** : Une routine BigQuery transforme les données brutes en tables structurées (Silver Layer).
4.  **Analyse de Sentiment** : Utilisation de modèles de Machine Learning (ou fonctions SQL avancées) pour classer les tweets (Positive, Neutral, Negative) dans BigQuery ML (Gold Layer).
5.  **Orchestration** : Le flux complet est piloté par **Apache Airflow** (Cloud Composer) pour garantir la résilience et le monitoring.
6.  **Visualisation** : Un tableau de bord **Looker Studio** permet d'explorer les résultats.

## ⚙️ Stack Technique
- **Orchestration** : Apache Airflow
- **Cloud Provider** : Google Cloud Platform (GCP)
- **Ingestion** : Cloud Functions, Pub/Sub
- **Data Warehouse** : BigQuery
- **Langage** : Python, SQL
- **Modélisation** : BigQuery ML / NLP basics

## 📂 Structure des fichiers
- `cloud_functions/` : Script d'ingestion des données Twitter.
- `dags/` : Définition des workflows Airflow.
- `bigquery/` : Scripts SQL pour les transformations et l'analyse de sentiment.
- `notebooks/` : Analyse exploratoire des données (EDA).

## 🚀 Fonctionnalités Clés
- **Automatisation Totale** : Ingestion quotidienne planifiée.
- **Scalabilité** : Architecture serverless capable de gérer de gros volumes de données.
- **Insights Actionnables** : Analyse de sentiment catégorisée.

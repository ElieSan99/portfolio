# Détection d'Anomalies E-commerce — Big Data & Time Series (Kering)

> [!NOTE]
> **Projet de Stage de Fin d'Études (Datafab pour Kering)**  
> *Le code source de ce projet est confidentiel et n'est pas publié dans ce portfolio. Ce document détaille la méthodologie, les technologies et les résultats obtenus.*

## - Contexte métier
Ce projet a été réalisé pour le groupe **Kering** (Luxe) dans le cadre d'un stage chez **Datafab**. L'enjeu était de surveiller les flux transactionnels des commandes des clients afin de détecter des anomalies (pics de ventes inhabituels, baisses injustifiées) en temps quasi-réel.

## - Problème à résoudre
Détecter des anomalies dans des séries temporelles à haute fréquence et fort volume, sans avoir de données étiquetées (approche **non supervisée**). Le système devait être capable de :
- Gérer des volumes de données massifs.
- S'adapter à la saisonnalité complexe du luxe (ventes privées, lancements).
- Réduire le nombre de fausses alertes pour les équipes opérationnelles.

## - Architecture & Stack Technique
Le projet repose sur une infrastructure Cloud robuste pour traiter la donnée à l'échelle :
- **Pré-traitement & Analyse :** **Apache Zeppelin (PySpark)** pour le nettoyage, l'agrégation de millions de lignes et l'exploration des données.
- **Modélisation :** Facebook **Prophet** (pour la baseline de saisonnalité) et **LSTM** (Deep Learning) pour capturer les dépendances temporelles complexes.
- **Orchestration & Déploiement :** **Vertex AI** (GCP) pour le suivi des modèles et la mise en production.

## - Approche technique : "Predictive Anomaly Detection"
L'approche retenue est une détection basée sur l'erreur de prédiction :
1.  **Modélisation de la normale :** Entraînement de modèles (Prophet/LSTM) pour prédire les valeurs futures attendues.
2.  **Calcul de l'écart :** Comparaison de la valeur réelle avec l'intervalle de confiance prédit.
3.  **Score d'anomalie :** Utilisation d'un seuil statistique (basé sur la distribution de l'erreur) pour déclencher une alerte si l'écart est trop important.

## - Déploiement & MLOps
- Mise en place de pipelines Vertex AI pour l'automatisation du ré-entraînement.
- Monitoring des performances du modèle pour éviter la dérive (drift).

## - Impact & Résultats
- Récupération et traitement de données massives.
- Réduction significative du temps de détection des incidents techniques sur le tunnel de vente.


## - Compétences clés démontrées
- **Big Data & Notebooks :** **PySpark**, **Apache Zeppelin** (Notebooks distribués).
- **Advanced Analytics :** Deep Learning pour séries temporelles (LSTM), Prophet.
- **Cloud/MLOps :** Maîtrise de l'écosystème Google Cloud (Vertex AI).

# Système de Trading Forex Multi-Agent Intelligent

## 🎯 Contexte métier
Le trading sur le marché du Forex nécessite une analyse constante de volumes de données massifs, une gestion du risque rigoureuse et une exécution rapide. Les systèmes traditionnels manquent souvent de flexibilité face aux changements de régime du marché.

Ce projet propose une architecture multi-agents où chaque composant est spécialisé dans une tâche critique (analyse, gestion du risque, exécution, audit), permettant une prise de décision plus robuste et adaptative.

## 🏗️ Architecture globale
Le système repose sur quatre agents autonomes orchestrés via **LangGraph** :
1.  **Flux Analyzer :** Analyse les indicateurs techniques et les flux de données.
2.  **Risk Strategist :** Définit la taille des positions et les stop-loss selon la volatilité.
3.  **Executor :** Gère l'envoi des ordres et le suivi de l'exécution.
4.  **Critic Agent :** Réalise l'auto-réflexion sur les performances passées pour ajuster les stratégies.

## ⚙️ Approche technique
*   **Deep Reinforcement Learning :** Modélisation du trading comme un problème de décision séquentielle (Gymnasium).
*   **RAG (Retrieval Augmented Generation) :** Utilisation de Pinecone pour stocker les profils de marché et enrichir le contexte des agents.
*   **Stack MLOps :** Docker pour la portabilité, Prometheus pour le monitoring des performances financières.

## 🚀 Impact & Résultats
*   Exécution automatisée 24/7 sur les paires de devises majeures.
*   Optimisation du ratio de Sortino grâce à l'ajustement dynamique du risque.
*   Architecture modulaire permettant l'ajout facile de nouveaux types d'analyses (Sentiment, Macro, etc.).

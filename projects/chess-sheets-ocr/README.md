# Reconnaissance Optique de Caractères (OCR) pour Feuilles de Match d'Échecs

🌟 **Vision du Projet**  
Ce projet, réalisé dans le cadre d'un stage à l'ECAM Rennes, visait à automatiser la numérisation des parties d'échecs à partir de feuilles de notation manuscrites. L'enjeu était de transformer un document papier complexe en un format numérique exploitable (PGN) pour permettre l'analyse informatique immédiate des parties.

💼 **Enjeux & Missions**
- **Automatisation de la Saisie** : Suppression de la saisie manuelle fastidieuse et sujette aux erreurs après les tournois.
- **Traitement de l'Écriture Manuscrite** : Relever le défi de la variabilité des écritures des joueurs sous pression.
- **Fiabilité Algorithmique** : Garantir que la séquence de coups reconstituée est légale selon les règles du jeu d'échecs.

🚀 **Réalisations Techniques**
- **Prétraitement d'Image Avancé (OpenCV)** : Nettoyage des scans, correction de perspective, segmentation des grilles de notation et extraction des cases individuelles.
- **Deep Learning (TensorFlow/Python)** : Entraînement d'un réseau de neurones convolutifs (CNN) spécialisé dans la reconnaissance de caractères manuscrits (chiffres et lettres spécifiques à la notation algébrique).
- **Algorithmique de Reconstitution** : Développement d'un moteur logique capable de réassembler les caractères détectés en coups cohérents, incluant la gestion des ambiguïtés et la validation des coups via les règles d'échecs.

🛠️ **Stack Technique**
- **Langage** : Python
- **Computer Vision** : OpenCV (Segmentation, Filtrage, Morphologie)
- **Intelligence Artificielle** : TensorFlow (Conception et entraînement du CNN)
- **Algorithmique** : Logique métier pour la validation des séquences de jeu.

📈 **Impact & Apports**
- **Expertise Vision par Ordinateur** : Maîtrise complète de la chaîne de traitement, du pixel brut à l'information structurée.
- **Rigueur Logique** : Capacité à coupler de l'IA (probabiliste) avec de l'algorithmique classique (déterministe) pour garantir 100% de cohérence métier.
- **Valorisation des Données** : Transformation d'archives physiques en base de données numériques prêtes pour l'analyse statistique ou l'entraînement de moteurs d'échecs.

---
> [!IMPORTANT]
> **NOTE : Confidentialité**  
> Le code source de ce projet a été réalisé dans un contexte professionnel et est soumis à une clause de confidentialité. Il ne peut donc pas être exposé publiquement. Ce dépôt sert de documentation technique pour présenter la méthodologie et les outils utilisés.

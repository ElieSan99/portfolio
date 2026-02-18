# Chess Sheets OCR — Numérisation automatisée de parties d'échecs

## - Contexte métier
Pour les clubs et les fédérations d'échecs, la saisie manuelle des feuilles de parties (notations algébriques) est une tâche chronophage et sujette aux erreurs. Ce projet vise à automatiser la conversion de ces documents manuscrits en formats numériques (PGN) exploitables par les moteurs d'analyse.

## - Problématiques Business Résolues
*   **Archivage de Masse :** Numérisation rapide de milliers de parties historiques.
*   **Intégrité des Données :** Utilisation de la logique du jeu pour corriger les erreurs de lecture OCR (ex: un coup impossible est automatiquement rectifié).
*   **Accessibilité :** Visualisation immédiate des parties sur échiquier numérique après scan.

## - Excellence Technique
*   **Computer Vision :** Prétraitement d'images (OpenCV) pour le redressement et le nettoyage des feuilles.
*   **Deep Learning (OCR) :** Reconnaissance des caractères manuscrits spécialisés (Symboles de pièces, chiffres, notation échecs).
*   **Validation Logique :** Intégration d'un moteur d'échecs (Stockfish/Chess.py) pour valider la légalité de chaque coup détecté.

## - Impact & Valeur Ajoutée
*   **Gain de temps :** Réduction de 90% du temps de saisie par partie.
*   **Portabilité :** Solution capable de s'adapter à différents formats de feuilles de notation.

# Utilisation d'une image Python légère
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers de dépendances
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source et des modèles
COPY src/ ./src/
COPY models/ ./models/

# Exposer le port sur lequel FastAPI va tourner
EXPOSE 8080

# Commande de lancement (Cloud Run utilise souvent le port 8080 par défaut)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]

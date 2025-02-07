#!/bin/bash

echo "🚀 Début du pipeline"

# Étape 1 : Récupération des données
echo "📥 Appel API et transformation en DataFrame..."
python etl_api.py

# Vérifier si l'étape précédente a réussi
if [ $? -ne 0 ]; then
  echo "❌ Erreur lors de l'appel API !"
  exit 1
fi

# Étape 2 : Traitement des données
echo "🛠️ Traitement du DataFrame..."
python eda.py

if [ $? -ne 0 ]; then
  echo "❌ Erreur lors du traitement des données !"
  exit 1
fi

echo "✅ Pipeline terminé avec succès !"

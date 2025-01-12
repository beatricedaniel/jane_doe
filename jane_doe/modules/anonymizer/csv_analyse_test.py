import pandas as pd
import os
from presidio_analyzer import AnalyzerEngine

# Initialisation de l'AnalyzerEngine
analyzer = AnalyzerEngine()

# Définir le chemin du dossier contenant les fichiers CSV
input_folder = "../../data/output"
output_folder = "./presidio_output"
os.makedirs(output_folder, exist_ok=True)

# Fonction pour analyser une valeur et déterminer si elle contient une entité
def contains_entity(value):
    if pd.isna(value):
        return "non"
    results = analyzer.analyze(text=value, entities=None, language="en")
    return "oui" if results else "non"

# Parcourir les fichiers CSV dans le dossier
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        # Lire le fichier CSV
        file_path = os.path.join(input_folder, file_name)
        df = pd.read_csv(file_path)

        # Vérifier que le fichier contient les colonnes attendues
        if df.shape[1] < 2:
            print(f"Le fichier {file_name} ne contient pas les colonnes attendues. Ignoré.")
            continue

        # Ajouter une nouvelle colonne basée sur l'analyse
        df["Est une entité?"] = df.iloc[:, 0].apply(contains_entity)

        # Sauvegarder le fichier CSV avec les résultats
        output_file_path = os.path.join(output_folder, file_name)
        df.to_csv(output_file_path, index=False)
        print(f"Traitement terminé pour {file_name}. Résultats enregistrés dans {output_file_path}.")

print("Analyse terminée pour tous les fichiers.")

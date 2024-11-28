import requests
import os

API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
# API key ajoutée directement ici
headers = {"Authorization": "Bearer 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"}

def query(filename):
    # Vérifie si le fichier existe
    if not os.path.exists(filename):
        print(f"Erreur : Le fichier {filename} n'existe pas.")
        return None

    # Lecture et envoi de l'image à l'API
    with open(filename, "rb") as f:
        data = f.read()

    response = requests.post(API_URL, headers=headers, data=data)

    # Vérifie si la requête a été réussie
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur API : {response.status_code} - {response.text}")
        return None

# Nom du fichier image à analyser
filename = "C:/Users/edoua/PycharmProjects/projet_IA/poisson.jpg"
output = query(filename)

# Affiche le résultat si disponible
if output:
    print("Résultat de l'API :", output)

import os
import pickle
from sklearn.naive_bayes import GaussianNB
from pdfminer.high_level import extract_text

# Load the model and vocabularies
with open('datasets/models.gnb', 'rb') as f:
    gnb: GaussianNB = pickle.load(f)

with open("datasets/vocabulaires.txt", "r") as fichier:
    vocabulaires = [ligne.strip() for ligne in fichier.readlines()]
    

# Function to predict the category of a given PDF file
def prediction(chemin):
    prediction = []
    texte = extract_text(chemin)
    
    for vocabulaire in vocabulaires:
        prediction.append(1 if vocabulaire in texte else  0)

    resultat = gnb.predict([prediction])
    
    return resultat[0]
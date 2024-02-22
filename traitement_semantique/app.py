import os
import pickle
from sklearn.naive_bayes import GaussianNB

# Load the model and vocabularies
with open('datasets/models.gnb', 'rb') as f:
    gnb: GaussianNB = pickle.load(f)

with open("datasets/vocabulaires.txt", "r") as fichier:
    vocabulaires = [ligne.strip() for ligne in fichier.readlines()]
import nltk
import re
from itertools import chain
from nltk.corpus import wordnet as wn

# Fonction qui affiche les synonymes d'un mot
def synonyme(mot):
    # Obtenir tous les synsets du mot
    synsets = wn.synsets(mot)

    # Fusionner les lemmes de tous les synsets et éliminer les doublons
    synonyms = set(chain.from_iterable([synset.lemma_names() for synset in synsets]))

    # Prendre les 5 premiers éléments
    synonyms = list(synonyms)[:5]

    # Joindre les synonymes en une seule chaîne séparée par des virgules
    synonyms_str = ', '.join(synonyms)

    print("\n", mot, " = ", synonyms_str)
    

# Fonction qui affiche une definition d'un mot
def definition(mot):
    # Trouver tous les synsets du mot
    synsets = wn.synsets(mot)

    # Afficher la definition du premier synonyme
    if synsets:
        print(mot, " : ", synsets[0].definition())
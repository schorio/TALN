import nltk
import re
from itertools import chain
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords


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
        
        
# Fonction principal
def traitement(nom_fichier): 
    
    # Charger les contenus d'un fichier texte
    t_txt = open(nom_fichier, "r")
    Text_txt = t_txt.read()
    text_txt = (Text_txt).lower()
    
    # Importation des stopwords en anglais
    stop_words = set(stopwords.words('english'))
    
    # Tokenisation
    tokens = nltk.word_tokenize(text_txt)
    tokens = [token for token in tokens if token not in stop_words]
    
    # supression du caractere speciaux de chaque mot du tableau
    mots = []
    for j in tokens:
        text = re.sub(r"[^a-zA-Zéèçêù$âäëöôüû]","",j)
        mots.append(text)
        
    # supression des emplacement libre dans le tableau
    liste_mots = list(filter(lambda x: x!="",mots))
    
    # Afficher le nombre de mot touver
    print("\n le nb de mot trouver : " , len(liste_mots))
    
    # Affchage du synonyme et definition de chaque mot trouver
    for mot in liste_mots:
        synonyme(mot)
        definition(mot)
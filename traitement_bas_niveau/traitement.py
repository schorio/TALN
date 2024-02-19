import re
    

def extraction(text):
    text = text.lower()

    # ajout des mots dans le tableau result
    result = re.split("\s", text)

    # supression des emplacement libre dans la liste
    liste_mots = list(filter(lambda x: x!="",result))

    # Afficher les nombres de mot
    print("\n Nombe des mots : ", len(liste_mots))
    
    # Calcul de la moyenne de la longueur des mots
    moyenne_longueur = sum(len(mot) for mot in liste_mots) / len(liste_mots) if liste_mots else 0
    print("\n Moyenne de la longueur des mots : ", moyenne_longueur)
    

def traitement(nom_fichier): 
    t_txt = open(nom_fichier, "r")
    Text_txt = t_txt.read()
    text_txt = (Text_txt).lower()
    extraction(text_txt)
    

traitement('texte.txt')
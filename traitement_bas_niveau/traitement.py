import re
    

def extraction(text):
    text = text.lower()

    # ajout des mots dans le tableau result
    result = re.split("\s", text)

    # supression des emplacement libre dans la liste
    liste_mots = list(filter(lambda x: x!="",result))

    # Afficher les nombres de mot
    print("\n Nombe des mots : ", len(liste_mots))
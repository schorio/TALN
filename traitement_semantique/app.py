import os
import pickle
from sklearn.naive_bayes import GaussianNB
from pdfminer.high_level import extract_text
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, Label

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

# Function to run the prediction on all PDF files in a directory
def run_prediction():
    dossier = filedialog.askdirectory(title="Selectionner le dossier à traiter")
    titres = []
    verif = []
    
    for i, nom_fichier in enumerate(os.listdir(dossier)):
        titres.append(nom_fichier)
        if nom_fichier.endswith('.pdf'):
            chemin = os.path.join(dossier, nom_fichier)
            resultat = prediction(chemin)
            verif.append(resultat)
            
            # Update the text widget with the result of the current file
            result_text.insert(ctk.END, f"{nom_fichier} = {resultat}\n")
            
            # Update the GUI
            root.update()






# Create the main application window
root = ctk.CTk(fg_color="black")
root.title("FilTra")
root.geometry("400x720")

image = Image.open('datasets/logo.png')
image = image.resize((250, 250))
photo = ImageTk.PhotoImage(image)
bouton = Label(root, image=photo, borderwidth=0)
bouton.pack()

result_text = ctk.CTkTextbox(root, width=300, height=300)
result_text.pack(padx=10, pady=10)

button = ctk.CTkButton(root, text="Parcourir", command=run_prediction)
button.pack(padx=10, pady=10)


# Start the main event loop
root.mainloop()

import os
import pickle
from sklearn.naive_bayes import GaussianNB
from pdfminer.high_level import extract_text
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import Label

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






# Create the main application window
root = ctk.CTk(fg_color="black")
root.title("FilTra")
root.geometry("400x720")

image = Image.open('datasets/logo.png')
image = image.resize((250, 250))
photo = ImageTk.PhotoImage(image)
bouton = Label(root, image=photo, borderwidth=0)
bouton.pack()


# Start the main event loop
root.mainloop()

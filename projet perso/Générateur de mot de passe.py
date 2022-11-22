#projet == Création d'un programme qui es un fast finger mais version pokémon
import random
from tkinter import *
#Création de la fenêtre
root = Tk()
#Personnalisation de la fenêtre
root.title("Générateur de mot de passe ")
root.geometry("500x500")
root.iconbitmap("projet perso\logoico.ico")
root.minsize(100,100)
root.maxsize(1000,1000)
root.config(background="orange")
# la fonction qui génère le mot de passe

caract_maj = "AZERTYUIOPQSDFGHJKLMWXCVBN"
caract_min = "azertyuiopqsdfghjklmwxcvbn"
caract_chif = "1234567890"
caract_spe = "!#*%:"

caractere = caract_chif + caract_maj + caract_min + caract_spe
length_for_pass = 12
def generateur(caractere, length_for_pass):
    passwords = "".join(random.sample(caractere, length_for_pass))
    print(f"Le mots de passe est : {passwords}")
#crée la boite du bouton qui active la fonction
boitefonction = Frame(root, bg="white")
boitefonction.pack(expand=YES)
bouton = Button(boitefonction, text="Générer", command=generateur(caractere, length_for_pass))
#crée la boite qui return le mot de passe
boite = Frame(root, bg="Black")
boite.pack()
root.mainloop()
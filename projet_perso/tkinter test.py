from tkinter import *
import webbrowser

def open_youtube():
    webbrowser.open_new("https://www.youtube.com/")
#Créer une première fenêtre
window = Tk()
#personnaliser cette fenêtre
window.title("Générateur de Bitcoin Facile et GRATUIT 100% no fake")
window.geometry("400x500")
window.minsize(300, 300)
window.maxsize(1080, 720)
window.config(background="orange")
#creer la boite
frame = Frame(window, bg="yellow")
#ajouter un texte
label_title = Label(frame, text="VASI VIEN", font=("Pixel",40), bg="yellow", fg="black")
label_title.pack(expand= YES)
#ajouter un second texte
label_sub_title = Label(frame, text="VASI VIEN", font=("Courrier",25), bg="yellow", fg="white")
label_sub_title.pack(expand= YES)
#ajouter un bouton
unbouton = Button(frame, text="SALUT BEBOU", font=("Courrier", 15), bg="white", fg="red", command=open_youtube)
unbouton.pack(pady= 25, fill=X)
#ajouter la boite
frame.pack(expand=YES)
#afficher
window.mainloop()
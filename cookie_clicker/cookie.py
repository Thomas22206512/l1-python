from tkinter import *
def compteur(x):
    return x+1
    
root = Tk()
root.geometry("600x600")
root.minsize(600, 600)
root.maxsize(1000, 1000)
root.title("Cookie Clicker du pauvre")
root.iconbitmap("cookie_clicker\cookie.ico")
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=compteur)
file_menu.add_command(label="On se casse", command=root.quit)
menu_bar.add_cascade(label="ALLER", menu=file_menu)
root.config(menu=menu_bar)
imagecookie = PhotoImage(file="cookie_clicker\cookie.png").zoom(40).subsample(32)
width, height = 500, 500
canvas = Canvas(root, width=width, height=height, bg="orange")
canvas.create_image(width/2, height/2, image=imagecookie)
canvas.pack(expand=YES)
bouton = Button(canvas, command=compteur)



root.mainloop()
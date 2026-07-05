import tkinter as tk 
fenetre = tk.Tk()
fenetre.title("Portail de connexion")
fenetre.geometry("400x300")
label_mot_de_passe = tk.Label(fenetre, text="Mot de passe : ")
label_mot_de_passe.pack()
fenetre.mainloop()

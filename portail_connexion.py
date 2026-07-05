def verifier_mot_de_passe():
    entree_mot_de_passe = entry_mot_de_passe.get()
    if entree_mot_de_passe == "qwerty":
        label_resultat.config(text="Connexion réussie")
        label_resultat.pack()
    else:
        label_resultat.config(text="Mot de passe incorrect")
        label_resultat.pack()
import tkinter as tk 
fenetre = tk.Tk()
fenetre.title("Portail de connexion")
fenetre.geometry("400x300")
label_mot_de_passe = tk.Label(fenetre, text="Mot de passe : ")
label_mot_de_passe.pack()
entry_mot_de_passe = tk.Entry(fenetre, show="*")
entry_mot_de_passe.pack()
label_resultat = tk.Label(fenetre, text="")
label_resultat.pack()
se_connecter = tk.Button(fenetre, text="Se connecter", command=verifier_mot_de_passe)
se_connecter.pack()
fenetre.mainloop()





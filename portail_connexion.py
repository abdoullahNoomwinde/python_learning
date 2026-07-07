essai = 3
def verifier_mot_de_passe():
    global essai
    entree_mot_de_passe = entry_mot_de_passe.get()   
    if entree_mot_de_passe == "azerty":
        label_resultat.config(text="Connexion réussie", fg="green")
    else:
        essai -= 1
        label_resultat.config(text=f"Mot de passe incorrect\nIl vous reste {essai} essai(s)", fg="red")
        entry_mot_de_passe.delete(0, tk.END)
        entry_mot_de_passe.focus_set()
        if essai == 0:
            label_resultat.config(text="Vous avez dépassé le nombre d'essais autorisés.\nVeuillez réessayer dans 5 secondes.", fg="red")
            se_connecter.config(state="disabled")
            fenetre.after(5000, reactiver_bouton)

def reactiver_bouton():
    global essai
    essai = 3
    se_connecter.config(state="normal")
    entry_mot_de_passe.delete(0, tk.END)
    entry_mot_de_passe.focus_set()
    label_resultat.config(text="Vous pouvez essayer à nouveau.", fg="green")

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


#essai = 3
#while essai < 0:
#    print("Mot de passe incorrect /nIl vous reste", essai, "essai(s)")
#if essai == 0:
#    print("Vous avez dépassé le nombre d'essais autorisés.\nVeuillez réessayer dans 5 secondes.")

  




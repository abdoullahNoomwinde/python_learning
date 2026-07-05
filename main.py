mot_de_passe = "qwerty"
tentatives_restantes = 3
while tentatives_restantes > 0 :
    mot_de_passe_1 = input("Saisissez votre mot de passe : ")
    if mot_de_passe_1 == mot_de_passe :
     print("Connexion reussie")
     break
    else :
     print("Mot de passe incorrect ")
     tentatives_restantes -= 1
     print("Tentatives restantes : ", tentatives_restantes)
if tentatives_restantes == 0 :
 print ("Compte bloqué")
 import time
temps = 10
while temps >= 0:
  print (temps, "s")
  time.sleep(1)
  temps -= 1
print ("Vous pouvez saisir a nouveau votre mot de passe")


poids = int(input("Combien de kg de fraises avez-vous acheté ? : "))
def prix (poids) :
    if poids <= 3 :
        prix = poids * 2.50
    else :
        prix = poids * 2
    return prix
facture = prix (poids)
print ("Votre facture est de", facture, "euros\nMerci pour votre achat !")

        
        
        
        
        
        
        
        
        







#print ("Votre facture est de", prix, "euros\nMerci pour votre achat !")


  
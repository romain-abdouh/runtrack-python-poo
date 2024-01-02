import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouvelle_valeur_rayon):
        self.rayon = nouvelle_valeur_rayon
        print("En changeant le rayon du cercle par", nouvelle_valeur_rayon,"les infos seront")

    def circonference(self):
        return 2 * math.pi * self.rayon
        
    
    def aire(self):
        return math.pi * (self.rayon ** 2)
        


    def diametre(self):
        return 2 * self.rayon
        
    
    def afficherInfos(self):
        print("Rayon du cercle :",self.rayon)
        print("Diamètre du cercle :", self.diametre())
        print("Circonférence du cercle :", self.circonference())
        print("Aire du cercle :", self.aire())

cercle1 = Cercle(4)
cercle1.afficherInfos()
cercle1.changerRayon(8)
cercle1.afficherInfos()

cercle2 = Cercle(7)
print ("Cercle numéro 2")
cercle2.afficherInfos()
        
  



       
        
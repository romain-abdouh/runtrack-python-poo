class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return  (self.TVA * self.prixHT) / 100 + self.prixHT
    
    def afficher (self):
        return self.nom , self.prixHT, self.TVA, self.CalculerPrixTTC()

    def changerNom (self, nouveau_nom):
        self.nom = nouveau_nom

    def changerPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix 

print("Informations initiales des produits :")
produit1 = Produit("T-shirt", 10, 20)
produit1.afficher()
print(produit1.nom)
print("Prix HT:",produit1.prixHT,"€")
print("TVA à ",produit1.TVA,"%")
print("Prix TTC",produit1.CalculerPrixTTC(),"€")
print("\n")

print("Nouveau nom produit")
produit1.changerNom("Pull")
produit1.afficher()
print(produit1.nom)
print("Prix HT:",produit1.prixHT,"€")
print("TVA à ",produit1.TVA,"%")
print("Prix TTC",produit1.CalculerPrixTTC(),"€")
print("\n")

print("Nouveau prix produit")
produit1.changerPrixHT(15)
produit1.afficher()
print(produit1.nom)
print("Prix HT:",produit1.prixHT,"€")
print("TVA à ",produit1.TVA,"%")
print("Prix TTC",produit1.CalculerPrixTTC(),"€")
print("\n")



produit2 = Produit("Smartphone", 1200, 20)
produit2.afficher()
print(produit2.nom)
print("Prix HT:",produit2.prixHT,"€")
print("TVA à ",produit2.TVA,"%")
print("Prix TTC",produit2.CalculerPrixTTC(),"€")
print("\n")


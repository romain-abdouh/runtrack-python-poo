class Commande:
    def __init__(self, numC, listDP, status="en cours"):
        self._numC = numC
        self._listDP = listDP
        self._status = status

    def get_numC(self):
        return self._numC

    def get_listDP(self):
        return self._listDP

    def get_status(self):
        return self._status

    def ajouter_plat(self, nom_plat, prix, statut="en cours"):
        plat = {"nom": nom_plat, "prix": prix, "statut": statut}
        self._listDP.append(plat)

    def annuler_commande(self):
        self._status = "annulée"
        print("Commande", self._status)

    def terminer_commande(self):
        self._status = "terminée"
        print("Commande", self._status)

    def calculer_total(self):
        total = 0
        for plat in self._listDP:
            total += plat["prix"]
        return total

    def calculer_tva(self, taux_tva=0.20):
        return self.calculer_total() * taux_tva

    def afficher_commande(self):
        print("Commande n°", self._numC, "statut: ", self._status)
        print("Plats commandés:")
        for plat in self._listDP:
            print(plat['nom'], "- Prix:", plat['prix'], "- Statut:", plat['statut'])
        print("Total HTT:", self.calculer_total(), "€")
        print("Total TTC:", self.calculer_total() + self.calculer_tva(), "€")


commande1 = Commande(1, [])
commande1.ajouter_plat("Pizza", 15.50)
commande1.ajouter_plat("Hamburger", 18)
commande1.afficher_commande()




      
        



  



       
        
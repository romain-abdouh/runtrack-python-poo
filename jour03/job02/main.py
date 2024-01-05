class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=True):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom 
        self._solde = solde
        self.decouvert = decouvert
        
    def afficher(self):
        print("Numéro compte:",self._numero_compte,"Nom:", self._nom,"Prénom:", self._prenom, "solde", self._solde,"€")

    def get_afficherSolde(self):
        return self._solde
    def set_afficherSolde(self, solde):
        print("Solde:", self._solde,"€")

    def get_versement(self):
        return self._solde
    def set_versement(self, versement):
        self._solde += versement
        print("Versement de", versement, "€ effectué. Nouveau solde:", self._solde, "€")

    def retrait(self, montant):
        if montant <= self._solde or self.decouvert:
            self._solde -= montant
            print("Retrait de", montant, "€ effectué. Nouveau solde:", self._solde, "€")
        else:
            print("Opération annulée. Solde insuffisant pour effectuer le retrait.")

    def autoriser_decouvert(self, autoriser=True):
        if autoriser:
            print("Autorisation de découvert accordée.")
        else:
            print("Decouvert non autorisé.")

    def agios(self, taux_agios):
        if self._solde < 0:
            agios = abs(self._solde) * (taux_agios / 100 )
            self._solde -= agios
            print("Agios de", agios, "%"" appliqués. Nouveau solde:", self._solde, "€")

    def virement(self, compte_dest, montant):
        if montant <= self._solde or self.decouvert:
            self._solde -= montant
            compte_dest.set_versement(montant)
            print("Virement de", montant, "€ depuis", self._nom,"effectué vers le compte", compte_dest._numero_compte)
        else:
            print("Opération annulée. Solde insuffisant pour effectuer le virement.")
    

compte = CompteBancaire(5454, "Josh", "jojo", 400)
compte.afficher()
compte.get_afficherSolde()
compte.set_versement(100)
compte.retrait(200)
print("\n")
compte2 = CompteBancaire(5455, "Dupond", "Bertrand", -100)
compte2.autoriser_decouvert()
compte2.afficher()
compte2.agios(5)
compte.virement(compte2, 110)
compte.afficher()
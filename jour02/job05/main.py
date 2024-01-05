class Voiture:
    def __init__(self, marque, modele, annee, km, reservoir, en_marche=False):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._km = km
        self._reservoir = reservoir
        self.en_marche = en_marche
        
    def demarrer(self):
        if not self.en_marche and self._verifier_plein():  
            self.en_marche = True
            print("La voiture démarre.")
        else:
            print("Pas assez de carburant pour démarrer")

    def arreter(self):
        if self.en_marche:
            self.en_marche = False
            print("La voiture s'arrête.")

    def get_marque(self):
        return self._marque
    def set_marque(self, marque):
        self._marque = marque

    def get_modele(self):
        return self._modele
    def set_modele(self, modele):
        self._modele = modele

    def get_annee(self):
        return self._annee
    def set_annee(self, annee):
        self._annee = annee

    def get_km(self):
        return self._km
    def set_km(self, km):
        self._km = km

    def _verifier_plein(self):
        return self._reservoir > 5
        
voiture = Voiture("AUDI", "RS4", 2012, 50000, 50)
voiture.demarrer()

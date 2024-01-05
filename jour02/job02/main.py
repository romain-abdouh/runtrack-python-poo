class Livre:
    def __init__(self, titre, auteur, nbP):
        self._titre = titre
        self._auteur = auteur
        self._nbP = nbP

    def get_titre(self):
        return self._titre
    def set_titre(self, titre):
        self._titre = titre
        
    def get_auteur(self):
        return self._auteur 
    def set_auteur(self, auteur):
        self._auteur = auteur

    def get_nbP(self):
        return self._nbP
    def set_nbP(self, nbP):
        if isinstance(nbP, int) and nbP > 0:
            self._nbP = nbP
        else:
            print("Erreur : Le nombre de page doit être un nombre entier positif.")

bouquin = Livre("Test", "Test", 10)
print(bouquin.get_titre())
print(bouquin.get_auteur())
print(bouquin.get_nbP())

print("\nTest changement nombre de pages")
bouquin.set_nbP(12)
print(bouquin.get_nbP())




    
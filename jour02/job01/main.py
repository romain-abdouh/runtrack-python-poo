class Rectangle:
    def __init__(self, longueur, largeur):
        self._longeur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longeur
    
    def set_longueur(self, longueur):
        self._longueur = longueur

    def get_largeur(self):
        return self._largeur
    
    def set_largeur(self, largeur):
        self._largeur = largeur

rectangle = Rectangle(10, 5)
print("Longueur:",rectangle.get_longueur())
print("Largeur:",rectangle.get_largeur())

rectangle.set_longueur(15)
rectangle.set_largeur(7)
print("Nouvelle longueur:", rectangle.get_longueur())
print("Nouvelle largeur:", rectangle.get_largeur())
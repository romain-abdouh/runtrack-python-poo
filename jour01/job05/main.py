class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("Les coordonnées du point sont", self.x, self.y)

    def afficherX(self):
        print("Coordonnée de x :", self.x)

    def afficherY(self):
        print("Coordonnée de y :", self.y)

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y
  
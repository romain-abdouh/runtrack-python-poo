class Livre:
    def __init__(self, titre, disponible=True):
        self.titre = titre
        self._disponible = disponible

    def vérification(self):
        return self._disponible

    def emprunter(self):
        if self.vérification():
            print("Le livre",self.titre,"a été emprunté.")
            self._disponible = False
        else:
            print("Le livre", self.titre, "n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.vérification():
            print("Le livre",self.titre, "a été rendu.")
            self._disponible = True
        else:
            print("Le livre", self.titre, "n'a pas été emprunté. Impossible de le rendre.")

livre1 = Livre("Blabla")

print("Le livre", livre1.titre, "est disponible :", livre1.vérification())
livre1.emprunter()
livre1.emprunter()
livre1.rendre()
print("Le livre", livre1.titre, "est disponible.")
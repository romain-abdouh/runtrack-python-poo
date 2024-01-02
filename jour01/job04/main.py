class Personne ():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis", self.nom, self.prenom)


personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")
personne1.SePresenter()
personne2.SePresenter()
  



       
        
class Ville:
    def __init__(self, nom, nombre_habitants):
        self._nom = nom
        self._nombre_habitants = nombre_habitants

    def get_nom(self):
        return self._nom

    def get_nombre_habitants(self):
        return self._nombre_habitants
    
    def augmenter_population(self):
        self._nombre_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville
        
    def get_nom(self):
        return self._nom
    
    def get_age(self):
        return self._age
    
    def get_ville(self):
        return self._ville.get_nom()
      
    def ajouter_population(self):
        self._ville.augmenter_population()
    
Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)
John = Personne("John", 26, Paris)
Myrtille = Personne("Myrtille", 26, Paris)
Chloe = Personne("Chloé", 18, Marseille)

print(Marseille.get_nom(), Marseille.get_nombre_habitants(), "habitants")
print(Paris.get_nom(), Paris.get_nombre_habitants(), "habitants")
John.ajouter_population()
Myrtille.ajouter_population()
Chloe.ajouter_population()
print("Mise à jour de la population de la ville de", Paris.get_nom(), ":", Paris.get_nombre_habitants(), "habitants")
print("Mise à jour de la population de la ville de", Marseille.get_nom(), ":", Marseille.get_nombre_habitants(), "habitants")

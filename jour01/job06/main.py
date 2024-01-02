class Animal:
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.vieillisement = self.age + 1
    
    def nommer (self):
        self.prenom = "Luna"
         

instance_animal = Animal(0, "chien")
print("L'age de l'animal", instance_animal.age)
instance_animal.vieillir()
print("L'age de l'animal", instance_animal.vieillisement)
instance_animal.nommer()
print("L'animal se nomme", instance_animal.prenom)



  



       
        
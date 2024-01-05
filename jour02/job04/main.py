class Student:
    def __init__(self, nom, prenom, numE, credits, level):
        self._nom = nom
        self._prenom = prenom
        self._numE = numE
        self._credits = credits
        self._level = self._studentEval(credits)

    def get_add_credits(self):
        return self._credits
    def set_add_credits(self, newCredits):
        if newCredits > 0:
            self._credits += newCredits
        else:
            print("Erreur : La valeur doit etre supérieur à 0.")

    def get_nom(self):
        return self._nom
    def set_nom(self, nom):
        self._nom = nom

    def get_prenom(self):
        return self._prenom
    def set_prenom(self, prenom):
        self._prenom = prenom

    def get_numE(self):
        return self._numE
    def set_numE(self, numE):
        self._numE = numE

    def get_credits(self):
        return self._credits
    def set_credits(self, credits):
        self._credits = credits

    def _studentEval(self, credits):
        if credits >= 90:
            return "Excellent"
        elif credits >= 80:
            return "Très bien"
        elif credits >= 70:
            return "Bien"
        elif credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    def get_studentEval(self):
        return self._studentEval(self._credits)

etudiant = Student("Doe", "John", 150251, 0, 0)
etudiant.set_add_credits(10)
etudiant.set_add_credits(10)
etudiant.set_add_credits(10)
print("Le nombre de crédits de",etudiant.get_prenom(), etudiant.get_nom(), "est de", etudiant.get_credits(),"points")

etudiant.set_add_credits(40)
print("Nom:", etudiant.get_nom())
print("Prenom:", etudiant.get_prenom())
print("Id:", etudiant.get_numE())
print("Niveau = ", etudiant.get_studentEval())
        

    
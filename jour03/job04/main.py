class Joueur:
    def __init__(self, nom, numero, position, nombre_but_marque, passe_decisive, carton_jaune, carton_rouge):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nombre_but_marque = nombre_but_marque
        self.passe_decisive = passe_decisive
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge
        
    def get_marquerUnBut(self):
        return self.nombre_but_marque
    def set_marquerUnBut(self, marquer):
        self.nombre_but_marque = marquer + self.nombre_but_marque
    
    def get_effectuerUnePasseDecisive(self):
        return self.passe_decisive
    def set_effectuerUnePasseDecisive(self, passe_decisive):
        self.passe_decisive = passe_decisive + self.passe_decisive
    
    def get_recevoirUnCartonJaune(self):
        return self.carton_jaune
    def set_recevoirUnCartonJaune(self, jaune):
        self.carton_jaune = jaune + self.carton_jaune

    def get_recevoirUnCartonRouge(self):
        return self.carton_rouge
    def set_recevoirUnCartonRouge(self, rouge):
        self.carton_rouge = rouge + self.carton_rouge
    
    def afficherStatistiques(self):
        print("Nom:", self.nom,"But:", self.nombre_but_marque,"Passe Décisives:", self.passe_decisive,"Carton jaune:", self.carton_jaune,"Carton rouge:", self.carton_rouge )
    
class Equipe:
    def __init__(self, nom, liste_joueurs=None):
        self.nom = nom
        self.liste_joueurs = [] if liste_joueurs is None else liste_joueurs

    def set_ajouter_joueur(self, ajouter_joueur):
        self.liste_joueurs.append(ajouter_joueur)

    def afficher_statistiques_joueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

David = Joueur("David", 10, "attaquant", 5, 1, 1, 0)
Vero = Joueur("Vero", 7, "defenseur", 0, 0, 2, 1)
Viktor = Joueur("Viktor", 11, "milieu", 2, 6, 0, 0)
Jojo = Joueur("Jojo", 11, "milieu", 12, 1, 5, 4)

Crystal = Joueur("Crystal", 10, "attaquant", 5, 1, 1, 0)
Elea = Joueur("Elea", 7, "defenseur", 0, 0, 2, 1)
Thomas = Joueur("Thomas", 11, "milieu", 2, 6, 0, 0)
Titi = Joueur("Titi", 11, "milieu", 12, 1, 5, 4)

equipe1 = Equipe("Équipe A", [David, Vero, Viktor])
equipe2 = Equipe("Équipe A", [Crystal, Elea, Thomas, Titi])
equipe1.set_ajouter_joueur(Jojo)

print("équipe 1")
equipe1.afficher_statistiques_joueurs()

print("équipe 2")
equipe2.afficher_statistiques_joueurs()

print("Nouvelle stats pour David")
David.set_recevoirUnCartonRouge(2)
David.set_marquerUnBut(1)
David.afficherStatistiques()

        
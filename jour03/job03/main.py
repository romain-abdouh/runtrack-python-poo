class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def get_titre(self):
        return self.titre 
    def set_titre(self, titre):
        self.titre = titre

    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
           
    def get_statut(self):
        return self.statut
    def set_statut(self, statut):
        self.statut = statut

    def afficher(self):
        print("Titre:", self.titre, "- Description:", self.description, "- Statut:", self.statut)


class ListeDeTaches:
    def __init__(self, taches=None):
        self.taches = [] if taches is None else taches

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, titre_tache):
        for x in self.taches:
            if x.get_titre() == titre_tache:
                self.taches.remove(x)
                print("Tâche",titre_tache, "supprimée de la liste.")
                return
        print("Tâche",titre_tache," non trouvée dans la liste.")

    def marquer_comme_finie(self, titre_tache):
        for x in self.taches:
            if x.get_titre() == titre_tache:
                x.set_statut("Terminée")
                print("Tâche",titre_tache, "terminée.")
                return
        print("Tâche",titre_tache," non trouvée dans la liste.")

    def afficher_liste(self):
        for x in self.taches:
            x.afficher()

tache1 = Tache("Courses", "blabla", "À faire")
tache2 = Tache("Ranger", "blabla", "À faire")
tache3 = Tache("Sortir", "blabla", "À faire")
liste_taches = ListeDeTaches([tache1, tache2, tache3])

liste_taches.afficher_liste()
print("\n")

liste_taches.marquer_comme_finie("Courses")
print("\n")

liste_taches.afficher_liste()

liste_taches.supprimer_tache("Sortir")

liste_taches.afficher_liste()
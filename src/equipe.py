class Equipe:
    def __init__(self, nom_equipe):
        self.nom_equipe =nom_equipe
        self.liste_joueurs = [] #ici on stockera des objets joueur
    def ajouter_joueur(self, joueur):
            self.liste_joueurs.append(joueur) 
            print(f"Le joueur {joueur.pseudo} a rejoint l'équipe {self.nom_equipe} . ")

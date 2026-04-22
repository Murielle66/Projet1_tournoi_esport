from match import Match

class Tournoi:
    def __init__(self, nom, liste_equipes):
        self.nom= nom
        self.equipes= liste_equipes # Liste d'objet Equipe
        self.matchs_demi= []
        self.match_finale =  None
    def generer_demies(self):
        # on crée deux matchs avec les 4 équipes
        print(f"\n---Génération des demi-finales du tournoi{self.nom}---")
        match1 = Match(self.equipes[0],self.equipes[1])
        match2 = Match(self.equipes[2],self.equipes[3])
        self.matchs_demi= [match1, match2]
        return match1, match2
    def lancer_finale(self, gagnant1,gagnant2):
        print(f"\n--- GRANDE FINALE ---")
        self.match_finale = Match(gagnant1,gagnant2)
        return self.match_finale


        
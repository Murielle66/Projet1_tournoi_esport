from match import Match

class Tournoi:
    # Gère la logique de progression d'un tournoi e-sport
    def __init__(self, nom :str, liste_equipes: list):
        self._nom= nom
        self._equipes= liste_equipes # Liste d'objet Equipe
        self._matchs_demi= []
        self._match_finale =  None
    def generer_demies(self):
        # Créer les deux matchs  de demi_finales à partir de  4 équipes
        print(f"\n---Génération des matchs du tournoi{self._nom}---")
         # vérification de sécurité 
        if len(self._equipes)< 4 :
           print(f"Erreur : il faut au moins 4 équipes pour générer des demi-finales")
           return None
        
        match1 = Match(self._equipes[0],self._equipes[1])
        match2 = Match(self._equipes[2],self._equipes[3])
        self._matchs_demi= [match1, match2]
        return self._matchs_demi 
    def lancer_finale(self, gagnant1,gagnant2):
         # Créer le match de finale avec les vainqueurs des demies.
        print(f"\n--- GRANDE FINALE ---")
        if not gagnant1 or not gagnant2 :
            print(f"Erreur : Les deux finalistes doivent etre définis")
            return None
        
        self._match_finale = Match(gagnant1,gagnant2)
        return self._match_finale


        
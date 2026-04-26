from match import Match

class Tournoi:
    # Gère la logique de progression d'un tournoi e-sport
    def __init__(self, nom :str, liste_equipes: list):
        if len(liste_equipes) != 8:
            raise ValueError("Un tournoi standard nécessite exactement 8 équipes.")
        self._nom= nom
        self._equipes= liste_equipes # Liste d'objet Equipe
        self._quarts = []
        self._matchs_demi= []
        self._match_finale =  None
    def generer_quarts(self):
        #Crée les 4 matchs de quarts de finale. 
        print(f"\n--- Quarts de Finale : {self._nom}---")
        for i in range (0, 8, 2):
            match = Match(self._equipes[i], self._equipes[i+1])
            self._quarts.append(match)
        return self._quarts
    def generer_demies(self, gagnants_quarts: list):
        # Créer les deux matchs  de demi_finales à partir des vainqueurs des quarts
         # vérification de sécurité 
        if len(gagnants_quarts) != 4 :
           raise ValueError(f"Format invalide : 4 vainqueurs requises.")
        print(f"\n---Demi-Finales---")
        
        match1 = Match(gagnants_quarts[0],gagnants_quarts[1])
        match2 = Match(gagnants_quarts[2],gagnants_quarts[3])
        self._matchs_demi= [match1, match2]
        return self._matchs_demi 
    def lancer_finale(self, gagnant_d1,gagnant_d2):
         # Créer le match de finale avec les vainqueurs des demies.
        print(f"\n--- GRANDE FINALE ---")
        
        self._match_finale = Match(gagnant_d1,gagnant_d2)
        return self._match_finale


        
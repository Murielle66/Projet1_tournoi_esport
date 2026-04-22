class Match:
    def __init__(self, equipe1, equipe2):
        self.equipe1 =equipe1
        self.equipe2 =equipe2
        self.vainqueur =None
    def designer_vainqueur(self, nom_vainqueur):
       if nom_vainqueur == self.equipe1.nom_equipe :
           self.vainqueur=self.equipe1
       else :
            self.vainqueur =self.equipe2
   

class Match:
    #Gère le déroulement et l'issue d'une confrontation entre deux équipes

    def __init__(self, equipe1, equipe2):
        if equipe1 == equipe2: 
            raise ValueError("Un match ne peut pas opposer une équipe à elle-meme.")
        self._equipe1 =equipe1
        self._equipe2 =equipe2
        self._vainqueur =None
        @property
        def vainqueur(self):
         # Retourne l'Objet Equipe qui a gagné le match .
         return self._vainqueur   
    def designer_vainqueur(self, nom_vainqueur :str):
       # Compare le nom saisi avec les noms des équipes pour désigner le gagnant.
       nom_saisi = nom_vainqueur.strip().lower()
       nom_e1 = self._equipe1.nom_equipe.strip().lower()
       nom_e2 = self._equipe2.nom_equipe.strip().lower()

       if nom_saisi == nom_e1 :
           self._vainqueur=self._equipe1
           print(f"Le vainqueur est :{self._equipe1.nom_equipe} ")
       elif nom_saisi == nom_e2:
            self._vainqueur =self._equipe2
            print(f"Le vainqueur est :{self._equipe2.nom_equipe} ")
       else:
           print(f" Erreur : Le Nom est invalide")
   

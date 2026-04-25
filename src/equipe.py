
class Equipe:
    #Représente une équipe d'e-sport composée de plusieurs joueurs
     def __init__(self, nom_equipe :str):
         self._nom_equipe = nom_equipe
         self._liste_joueurs = [] 
        #Stockage interne des objets joueur
     @property
     def nom_equipe(self):
          return self._nom_equipe
     @property
     def liste_joueurs(self):
        #Retourne la liste des joueurs
          return self._liste_joueurs
        
     def ajouter_joueur(self, joueur):
            #ajoute un objet joueur à l'équipe s'il n'y est pas déja
            if joueur in self._liste_joueurs:
                 print(f" ERREUR :Le joueur {joueur.pseudo} est déja dans l'équipe.")
                 return
            self._liste_joueurs.append(joueur) 
            print(f" SUCCES : Le joueur {joueur._pseudo} a rejoint l'équipe {self.nom_equipe} . ")

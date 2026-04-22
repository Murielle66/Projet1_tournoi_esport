from entites import Personne
class Joueur(Personne):
    #Représente le compétiteur e-sport
    def __init__(self, nom: str , pseudo: str): 
    # On appelle le constructeur de la classe parente (Personne)
     super().__init__(nom)
     self._pseudo = pseudo
     self.__score_total = 0 
     @property
     def pseudo(self):
        return self._pseudo
     @property
     def score_total(self):
        return self.__score_total
     
    def ajouter_points(self, points:int):
      #Incrémente le score si la valeur est positive
      if points > 0:
        self.__score_total += points
        print(f"Score mis à jour : {self._pseudo} a maintenant {self.__score}")
      else:
         print(f"Le nombre de points doit etre positif.")
    

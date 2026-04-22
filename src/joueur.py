class Joueur :
    def __init__(self, pseudo): 
     self.pseudo= pseudo
     self.__score_total=0 
    def ajouter_points(self, points):
       if points > 0:
          self.__score_total += points
    def obtenir_score(self):
       return self.__score_total

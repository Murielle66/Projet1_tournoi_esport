from entites import Personne
class Joueur(Personne):
    #Représente le compétiteur e-sport
     def __init__(self, nom: str , pseudo: str): 
    # On appelle le constructeur de la classe parente (Personne)
      super().__init__(nom)
      if not pseudo.strip(): 
        raise ValueError("Le pseudo ne peut pas etre vide .")
      self._pseudo = pseudo
      self.__score_total = 0 
     @property
     def pseudo(self):
        return self._pseudo
     @property
     def score_total(self):
        return self.__score_total
     
     def ajouter_points(self, points:int):
       #Incrémente le score avec gestion d'exception
      try:
        if points < 0:
         raise ValueError("Le score ne peut pas etre négatif.")
        self.__score_total += points
      except ValueError as e: 
          print(f"Erreur Qualité : {e}")
      
    

class Personne:
    #Représente une personne physique du système e-sport
    def __init__(self,nom :str):
     #On utilise le tiret bas pour l'encapsulation   
        self._nom = nom
    @property
    def nom(self):
        # Getter pour obtenir le nom de la personne
        return self._nom
class Organisatrice(Personne):
    # Gère l'organisation de tournoi,herite de personne
    def __init__(self, nom :str, role :str ="Admin"):
        super().__init__(nom)
        self.role = role

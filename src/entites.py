class Personne :
    def __init__(self,nom):
        self.nom =nom
class Organisatrice(Personne):# herite de personne
    def __init__(self, nom, role="Admin"):
        super().__init__(nom)
        self.role=role

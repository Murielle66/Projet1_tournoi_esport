from joueur import Joueur
from equipe import Equipe
#1. Création des joueurs
j1 = Joueur(" Zyro")
j2 = Joueur(" Keen")
#2. Création de l'équipe
ma_team =Equipe("Les Apex")
#3. Utilisation de la relation( Composition)
ma_team.ajouter_joueur(j1)
ma_team.ajouter_joueur(j2)
#4.Vérification
print(f"Nombre de joueurs dans l'équipe : {len(ma_team.liste_joueurs)}")
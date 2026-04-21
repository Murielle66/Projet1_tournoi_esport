from match import Match
from entites import Organisatrice
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
#5. Test de l'héritage
admin = Organisatrice("Murielle","Super-User")
print(f"Admin :{admin.nom}, Role : {admin.role}")
#6. Test de l'encapsulation
j1.ajouter_points(10)
print(f"Nouveau score de {j1.pseudo} : {j1.obtenir_score()} points")
#7. Test de la modularité
autre_team = Equipe("Aigles de cotonou")
nouveau_match = Match(ma_team, autre_team)
nouveau_match.designer_vainqueur("Les Apex")
print(f"Vainqueur du match : {nouveau_mach.vainqueur.nom_equipe}")
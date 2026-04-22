from match import Match
from entites import Organisatrice
from joueur import Joueur
from equipe import Equipe
from database import Database
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
admin = Organisatrice("Alex Carter","Super-User")
print(f"Admin :{admin.nom}, Role : {admin.role}")
#6. Test de l'encapsulation
j1.ajouter_points(10)
print(f"Nouveau score de {j1.pseudo} : {j1.obtenir_score()} points")
#7. Test de la modularité
autre_team = Equipe("Les Nexus")
nouveau_match = Match(ma_team, autre_team)
#print(f"Match entre {ma_team} et {autre_team}")
nouveau_match.designer_vainqueur("Les Apex")
print(f"Vainqueur du match : {nouveau_match.vainqueur.nom_equipe}")
#8. Initialisation de la base
db = Database()
#9. Sauvegarde des joueurs après match 
db.sauvegarder_joueur(j1)
db.sauvegarder_joueur(j2)
print(f">>> Données sauvegardées dans tournoi.db")
db.fermer
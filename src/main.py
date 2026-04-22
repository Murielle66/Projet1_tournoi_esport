from match import Match
from entites import Organisatrice
from joueur import Joueur
from equipe import Equipe
from database import Database
 #base de données
db = Database()
print(f"INITIALISATION DU TOURNOI E-SPORT")
anciens_joueurs = db.recuperer_tous_les_joueurs()
if anciens_joueurs:
 print(f"--- {len(anciens_joueurs)} Joueurs chargés depuis la base de données ---") 
 for pseudo , score in anciens_joueurs:
  print(f"Joueur : {pseudo}| Score: {score}")
 else:
  print(f"---Aucun joueur en base ,creation d'un nouveau tournoi---")

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
#9. Sauvegarde des joueurs après match 
 db.sauvegarder_joueur(j1)
 db.sauvegarder_joueur(j2)
# 10. Organisation du Tournoi 
# On crée 2 autres joueurs et une 2ème équipe pour avoir un vrai tournoi
j3, j4 = Joueur("Saitama"), Joueur("Genos")
team_b = Equipe("Les Nexus") 
team_b.ajouter_joueur(j3)
team_b.ajouter_joueur(j4)

# Liste des participants
participants = [ma_team, team_b, Equipe("Team C"), Equipe("Team D")] 

# Lancement de la logique de bracket
from tournoi import Tournoi
mon_tournoi = Tournoi("Gamer Arena", participants)
m1, m2 = mon_tournoi.generer_demies()
#m1.enregistrer_resultat(16,10)
#m2.enregistrer_resultat(14, 16)
gagnant1= m1.designer_vainqueur("Les Apex")
gagnant2= m1.designer_vainqueur("Les Nexus")

print(f"\n--- Brackets du Tournoi {mon_tournoi.nom} ---")
print(f"Demi-finale 1 : {m1.equipe1.nom_equipe} vs {m1.equipe2.nom_equipe}")

# Simulation de qualification automatique
m1.designer_vainqueur("Les Apex")
print(f"Qualifié pour la finale : {m1.vainqueur.nom_equipe}")

# 11. Sauvegarde finale et fermeture
db.sauvegarder_joueur(j3)
db.sauvegarder_joueur(j4)
print(f">>> Toutes les données du tournoi sont dans tournoi.db")
db.fermer()

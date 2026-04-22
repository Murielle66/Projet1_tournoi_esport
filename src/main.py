from match import Match
from entites import Organisatrice
from joueur import Joueur
from equipe import Equipe
from database import Database
from tournoi import Tournoi

# 1. base de données
db = Database()
print(f" INITIALISATION DU TOURNOI E-SPORT ")
anciens_joueurs = db.recuperer_tous_les_joueurs()
if anciens_joueurs:
 print(f"--- {len(anciens_joueurs)} Joueurs chargés depuis la base de données ---") 
 for pseudo , score in anciens_joueurs:
  print(f"Joueur : {pseudo}  | Score: {score}")
else:
  print(f"---Aucun joueur en base ,creation d'un nouveau tournoi---")

#2. Création des joueurs
j1 = Joueur("Zyro")
j2 = Joueur("Keen")
j3 = Joueur("Saitama")
j4 = Joueur("Genos")
j5 = Joueur("Raze")
j6 = Joueur("Nyx")
j7 = Joueur("Axel")
j8 = Joueur("Vyn")
#3. Création de l'équipe
ma_team =Equipe("Les Apex")
team_b = Equipe("Les Nexus")
team_c = Equipe("Les Vortex")
team_d = Equipe("Les Prime")
#4. Utilisation de la relation( Composition)
ma_team.ajouter_joueur(j1)
ma_team.ajouter_joueur(j2)
team_b.ajouter_joueur(j3)
team_b.ajouter_joueur(j4)
team_c.ajouter_joueur(j5)
team_c.ajouter_joueur(j6)
team_d.ajouter_joueur(j7)
team_d.ajouter_joueur(j8)

#5. Test de l'héritage
admin = Organisatrice("Alex Carter","Super-User")
print(f"Admin :{admin.nom}, Role : {admin.role}")

 #6. Organisation du Tournoi 

# Liste des participants
participants = [ma_team, team_b, team_c, team_d ]  
mon_tournoi = Tournoi(" Gamer Arena", participants)
# Lancement de la logique de bracket
m1, m2 = mon_tournoi.generer_demies()
m1.designer_vainqueur(m1.equipe1.nom_equipe)
gagnant1 = m1.vainqueur
m2.designer_vainqueur(m2.equipe1.nom_equipe)
gagnant2= m2.vainqueur

print("\n===================================")
print(f"  TOURNOI : {mon_tournoi.nom}")
print("=================================")

print(f"Demi-finale 1 : {m1.equipe1.nom_equipe} vs {m1.equipe2.nom_equipe}")
print(f" --- GAGNANT :  {gagnant1.nom_equipe} ---")
print(f"Demi-finale 2 : {m2.equipe1.nom_equipe} vs {m2.equipe2.nom_equipe}")
print(f" --- GAGNANT :  {gagnant2.nom_equipe} ---")
print(f"Finale : {gagnant1.nom_equipe} vs {gagnant2.nom_equipe}")

finale = mon_tournoi.lancer_finale(gagnant1, gagnant2)
finale.designer_vainqueur(gagnant1.nom_equipe)
print(f" Vainqueur : {finale.vainqueur.nom_equipe}")

# 9. Sauvegarde  et fermeturedb.sauvegarder_joueur(j1)
db.sauvegarder_joueur(j1)
db.sauvegarder_joueur(j2)
db.sauvegarder_joueur(j3)
db.sauvegarder_joueur(j4)
db.sauvegarder_joueur(j5)
db.sauvegarder_joueur(j6)
db.sauvegarder_joueur(j7)
db.sauvegarder_joueur(j8)
db.fermer()
print(f">>> Toutes les données du tournoi sont dans tournoi.db")


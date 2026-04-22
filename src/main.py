
from entites import Organisatrice
from joueur import Joueur
from equipe import Equipe
from database import Database
from tournoi import Tournoi

# 1. base de données
db = Database()
print(f"\n=== INITIALISATION DU TOURNOI E-SPORT === ")
anciens_joueurs = db.recuperer_tous_les_joueurs()
if anciens_joueurs:
 print(f"--- {len(anciens_joueurs)} Joueurs chargés depuis la base de données ---") 
 for pseudo , score in anciens_joueurs:
  print(f"Joueur : {pseudo}  | Score: {score}")
else:
  print(f"---Aucun joueur en base ,creation d'un nouveau tournoi---")

#2. Création des joueurs
# Format Joueur( "Nom reel","pseudo")
j1 = Joueur( "Wazyr" ,"Zyro")
j2 = Joueur( "jean" , "Keen")
j3 = Joueur( "Marc " ,"Saitama")
j4 = Joueur(" Bob" ,"Genos")
j5 = Joueur( "Alfred" ,"Raze")
j6 = Joueur( "Luc " ,"Nyx")
j7 = Joueur(" sam" ,"Axel")
j8 = Joueur("Vyncent", "Vyn")
#3. Création de l'équipe
equipes = [ 
 Equipe("Les Apex"),
 Equipe("Les Nexus"),
 Equipe("Les Vortex"),
 Equipe("Les Prime")
 ]
#4. Utilisation de la relation( Composition)
equipes[0].ajouter_joueur(j1)
equipes[0].ajouter_joueur(j2)
equipes[1].ajouter_joueur(j3)
equipes[1].ajouter_joueur(j4)
equipes[2].ajouter_joueur(j5)
equipes[2].ajouter_joueur(j6)
equipes[3].ajouter_joueur(j7)
equipes[3].ajouter_joueur(j8)

#5. Test de l'héritage
admin = Organisatrice("Mel Carter","Super-User")
print(f"\n Admin :{admin.nom}, Role : {admin.role}")

 #6. Organisation du Tournoi 
mon_tournoi = Tournoi(" Gamer Arena", equipes)
#7. Lancement de la logique de bracket
matchs = mon_tournoi.generer_demies()
if matchs: 
 m1, m2 =matchs
 #Simulation des victoires
m1.designer_vainqueur(m1._equipe1.nom_equipe)
m2.designer_vainqueur(m2._equipe1.nom_equipe)

print("\n" + "="*35)
print(f"  TOURNOI : {mon_tournoi._nom}")
print("\n" + "="*35)

''' print(f"Demi-finale 1 : {m1.equipe1.nom_equipe} vs {m1.equipe2.nom_equipe}")
print(f" --- GAGNANT :  {gagnant1.nom_equipe} ---")
print(f"Demi-finale 2 : {m2.equipe1.nom_equipe} vs {m2.equipe2.nom_equipe}")
print(f" --- GAGNANT :  {gagnant2.nom_equipe} ---")
print(f"Finale : {gagnant1.nom_equipe} vs {gagnant2.nom_equipe}") '''

finale = mon_tournoi.lancer_finale(m1._vainqueur, m2._vainqueur)
if finale: 
 finale.designer_vainqueur(m1._vainqueur.nom_equipe)
print(f" LE GRAND VAINQUEUR : {finale._vainqueur.nom_equipe}")

# 9. Sauvegarde  et fermeturedb.sauvegarder_joueur(j1)
liste_joueurs = [j1, j2, j3, j4, j5, j6, j7, j8]
for j in liste_joueurs: 
 db.sauvegarder_joueur(j)
db.fermer()
print(f"\n>>> Toutes les données du tournoi sont dans tournoi.db ")


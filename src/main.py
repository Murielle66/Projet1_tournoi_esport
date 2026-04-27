import sys
import os

# Configuration pour les imports 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import Database
from joueur import Joueur
from equipe import Equipe
from tournoi import Tournoi

def afficher_titre():
    print("\n" + "="*50)
    print("      SYSTÈME DE GESTION E-SPORT ")
    print("="*50)

def main():
    db = Database()
    equipes_creees = []  # Liste des équipes pour le tournoi en cours

    while True:
        afficher_titre()
        print(f" Statut : {len(equipes_creees)}/8 équipes prêtes")
        print("-" * 50)
        print("1. [JOUEURS] : Voir le classement / Ajouter un joueur")
        print("2. [ÉQUIPES] : Créer une équipe (2 joueurs uniques)")
        print("3. [TOURNOI] : Lancer le bracket (8 équipes requises)")
        print("4. [RESET]   : Réinitialiser la liste des équipes")
        print("5. [QUITTER] : Fermer l'application")
        
        choix = input("\nAction (1-5) : ")

        # --- OPTION 1 : GESTION DES JOUEURS ---
        if choix == "1":
            print("\n--- CLASSEMENT ACTUEL ---")
            joueurs = db.recuperer_tous_les_joueurs()
            if not joueurs:
                print("Aucun joueur en base.")
            else:
                for p, s in joueurs:
                    print(f"• {p.ljust(15)} | Points : {s}")
            
            sub = input("\nAjouter un nouveau joueur ? (o/n) : ")
            if sub.lower() == 'o':
                nom = input("Nom réel : ")
                pseudo = input("Pseudo unique : ")
                try:
                    db.sauvegarder_joueur(Joueur(nom, pseudo))
                    print("Joueur enregistré !")
                except ValueError as e:
                    print(f"Erreur : {e}")

        # --- OPTION 2 : CRÉATION ÉQUIPE AVEC VÉRIFICATION ---
        elif choix == "2":
            if len(equipes_creees) >= 8:
                print("Le tournoi est déjà complet (8 équipes).")
                continue
            
            # Identifier les joueurs déjà pris
            pseudos_occupes = [j.pseudo for eq in equipes_creees for j in eq.liste_joueurs]
            
            joueurs_db = db.recuperer_tous_les_joueurs()
            # Filtrer pour n'afficher que les joueurs libres
            disponibles = [j for j in joueurs_db if j[0] not in pseudos_occupes]

            if len(disponibles) < 2:
                print("Erreur : Pas assez de joueurs disponibles en base de données.")
                continue

            nom_e = input("\nNom de l'équipe : ")
            nouvelle_eq = Equipe(nom_e)
            
            print("\nJoueurs disponibles :")
            for i, (p, s) in enumerate(disponibles):
                print(f"{i}. {p} (Score: {s})")
            
            try:
                idx1 = int(input("Choisir Joueur 1 (index) : "))
                idx2 = int(input("Choisir Joueur 2 (index) : "))
                
                if idx1 == idx2:
                    print("Impossible de choisir deux fois le même joueur !")
                    continue

                # Création et ajout des objets joueurs
                j1 = Joueur("Inconnu", disponibles[idx1][0])
                j2 = Joueur("Inconnu", disponibles[idx2][0])
                
                nouvelle_eq.ajouter_joueur(j1)
                nouvelle_eq.ajouter_joueur(j2)
                equipes_creees.append(nouvelle_eq)
                print(f"Équipe {nom_e} validée !")
            except (ValueError, IndexError):
                print("Sélection invalide.")

        # --- OPTION 3 : LOGIQUE DU TOURNOI ---
        elif choix == "3":
            if len(equipes_creees) < 8:
                print(f"Action impossible : {len(equipes_creees)}/8 équipes.")
                continue
            
            try:
                t = Tournoi("Tournoi Bénin E-Sport", equipes_creees)
                
                # --- ÉTAPE : QUARTS ---
                print("\n>>> DÉBUT DES QUARTS DE FINALE")
                vainqueurs_q = []
                for m in t.generer_quarts():
                    print(f"\nMATCH : {m._equipe1.nom_equipe} VS {m._equipe2.nom_equipe}")
                    sc1 = int(input(f"Score {m._equipe1.nom_equipe} : "))
                    sc2 = int(input(f"Score {m._equipe2.nom_equipe} : "))
                    
                    v = m._equipe1 if sc1 > sc2 else m._equipe2
                    m.designer_vainqueur(v.nom_equipe)
                    vainqueurs_q.append(v)

                # --- ÉTAPE : DEMIES ---
                print("\n>>> DÉBUT DES DEMI-FINALES")
                matchs_d = t.generer_demies(vainqueurs_q)
                vainqueurs_d = []
                for m in matchs_d:
                    print(f"\nMATCH : {m._equipe1.nom_equipe} VS {m._equipe2.nom_equipe}")
                    sc1 = int(input(f"Score {m._equipe1.nom_equipe} : "))
                    sc2 = int(input(f"Score {m._equipe2.nom_equipe} : "))
                    
                    v = m._equipe1 if sc1 > sc2 else m._equipe2
                    m.designer_vainqueur(v.nom_equipe)
                    vainqueurs_d.append(v)

                # --- ÉTAPE : FINALE ---
                f = t.lancer_finale(vainqueurs_d[0], vainqueurs_d[1])
                print(f"\n*** GRANDE FINALE : {f._equipe1.nom_equipe} VS {f._equipe2.nom_equipe} ***")
                sc1 = int(input(f"Score {f._equipe1.nom_equipe} : "))
                sc2 = int(input(f"Score {f._equipe2.nom_equipe} : "))
                
                champion = f._equipe1 if sc1 > sc2 else f._equipe2
                f.designer_vainqueur(champion.nom_equipe)
                
                print(f"\nFÉLICITATIONS : {champion.nom_equipe} remporte le tournoi !")
                
                # Mise à jour des points en DB (Récompense)
                for joueur in champion.liste_joueurs:
                    joueur.ajouter_points(20) # Bonus victoire
                    db.sauvegarder_joueur(joueur)

            except Exception as e:
                print(f"Erreur durant le tournoi : {e}")

        elif choix == "4":
            equipes_creees = []
            print("Liste des équipes réinitialisée.")

        elif choix == "5":
            db.fermer()
            print("Fermeture sécurisée de la base de données. Au revoir !")
            sys.exit()

if __name__ == "__main__":
    main()
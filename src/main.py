import sys
import os

# Configuration pour les imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import Database
from joueur import Joueur
from equipe import Equipe
from tournoi import Tournoi

def afficher_titre():
    print("\n" + "="*45)
    print("      GESTIONNAIRE E-SPORT : EDITION 2026")
    print("="*45)

def main():
    db = Database()
    equipes_creees = [] # Stockage temporaire des équipes pour le tournoi

    while True:
        afficher_titre()
        print(f"Équipes prêtes : {len(equipes_creees)}/8")
        print("-" * 45)
        print("1. Gérer les Joueurs (Voir/Ajouter)")
        print("2. Créer une Équipe (Ajouter des joueurs)")
        print("3. Lancer le Tournoi (8 équipes requises)")
        print("4. Réinitialiser la liste des équipes")
        print("5. Quitter")
        
        choix = input("\nOption : ")

        # --- OPTION 1 : GESTION JOUEURS ---
        if choix == "1":
            print("\n[1] Liste des joueurs | [2] Ajouter un joueur")
            sub = input("Choix : ")
            if sub == "1":
                joueurs = db.recuperer_tous_les_joueurs()
                for p, s in joueurs: print(f"• {p} ({s} pts)")
            elif sub == "2":
                nom = input("Nom réel : "); pseudo = input("Pseudo : ")
                db.sauvegarder_joueur(Joueur(nom, pseudo))

        # --- OPTION 2 : CRÉER UNE ÉQUIPE ---
        elif choix == "2":
            if len(equipes_creees) >= 8:
                print("Nombre maximum d'équipes atteint !")
                continue
            
            nom_e = input("\nNom de la nouvelle équipe : ")
            nouvelle_equipe = Equipe(nom_e)
            
            print("Sélectionnez 2 joueurs pour cette équipe :")
            joueurs_db = db.recuperer_tous_les_joueurs()
            
            for i, (p, s) in enumerate(joueurs_db):
                print(f"{i}. {p}")
            
            try:
                idx1 = int(input("Index du joueur 1 : "))
                idx2 = int(input("Index du joueur 2 : "))
                
                # Récupération des objets Joueur
                j1 = Joueur("Inconnu", joueurs_db[idx1][0])
                j2 = Joueur("Inconnu", joueurs_db[idx2][0])
                
                nouvelle_equipe.ajouter_joueur(j1)
                nouvelle_equipe.ajouter_joueur(j2)
                equipes_creees.append(nouvelle_equipe)
                print(f"L'équipe {nom_e} est prête !")
            except (ValueError, IndexError):
                print("Erreur de sélection.")

        # --- OPTION 3 : LE TOURNOI (LOGIQUE DES SCORES) ---
        elif choix == "3":
            if len(equipes_creees) < 8:
                print(f"Erreur : Il faut 8 équipes (actuel: {len(equipes_creees)})")
                continue
            
            try:
                mon_tournoi = Tournoi("Championnat UP", equipes_creees)
                
                # -- QUARTS --
                print("\n--- QUARTS DE FINALE ---")
                vainqueurs_quarts = []
                for m in mon_tournoi.generer_quarts():
                    print(f"\nMATCH : {m._equipe1.nom_equipe} vs {m._equipe2.nom_equipe}")
                    s1 = int(input(f"Score {m._equipe1.nom_equipe} : "))
                    s2 = int(input(f"Score {m._equipe2.nom_equipe} : "))
                    
                    v = m._equipe1 if s1 > s2 else m._equipe2
                    m.designer_vainqueur(v.nom_equipe)
                    vainqueurs_quarts.append(v)
                    print(f"Qualifié : {v.nom_equipe}")

                # -- DEMIES --
                print("\n--- DEMI-FINALES ---")
                matchs_demi = mon_tournoi.generer_demies(vainqueurs_quarts)
                vainqueurs_demies = []
                for m in matchs_demi:
                    print(f"\nMATCH : {m._equipe1.nom_equipe} vs {m._equipe2.nom_equipe}")
                    s1 = int(input(f"Score {m._equipe1.nom_equipe} : "))
                    s2 = int(input(f"Score {m._equipe2.nom_equipe} : "))
                    
                    v = m._equipe1 if s1 > s2 else m._equipe2
                    m.designer_vainqueur(v.nom_equipe)
                    vainqueurs_demies.append(v)

                # -- FINALE --
                finale = mon_tournoi.lancer_finale(vainqueurs_demies[0], vainqueurs_demies[1])
                print(f"\n*** FINALE : {finale._equipe1.nom_equipe} vs {finale._equipe2.nom_equipe} ***")
                s1 = int(input(f"Score {finale._equipe1.nom_equipe} : "))
                s2 = int(input(f"Score {finale._equipe2.nom_equipe} : "))
                
                gagnant = finale._equipe1 if s1 > s2 else finale._equipe2
                finale.designer_vainqueur(gagnant.nom_equipe)
                
                print(f"\n CHAMPION : {gagnant.nom_equipe}")
                
                # Mise à jour des points des gagnants en DB
                for joueur in gagnant.liste_joueurs:
                    joueur.ajouter_points(10)
                    db.sauvegarder_joueur(joueur)

            except Exception as e:
                print(f"Erreur tournoi : {e}")

        elif choix == "4":
            equipes_creees = []
            print("Liste des équipes réinitialisée.")

        elif choix == "5":
            db.fermer()
            sys.exit()

if __name__ == "__main__":
    main()
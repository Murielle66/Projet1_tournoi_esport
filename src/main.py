
from entites import Organisatrice
from joueur import Joueur
from equipe import Equipe
from database import Database
from tournoi import Tournoi

def afficher_menu():
    print(f"\n=== GESTIONNAIRE E-SPORT ===")
    print(f"1. Enregistrer un nouveau joueur")
    print(f"2. Créer une équipe")
    print(f"3. Lancer un tournoi (4 équipes requises)")
    print(f"4. Afficher les stats des joueurs")
    print(f"5. Quitter")
    return input("Choisissez une option : ")
def main():
    db = Database()
    try:
        while True:
            choix = afficher_menu()
            if choix == "1":
                nom = input("Nom réel du joueur: ")
                pseudo = input("Pseudo : ")
                nouveau_j = Joueur(nom, pseudo)
                db.sauvegarder_joueur(nouveau_j)
                print(f"Joueur{pseudo} enregistré avec succès !")
            elif choix == "2":
                nom_e = input("Nom de l'équipe : ")
                equipe = Equipe(nom_e)
                print(f"Equipe {nom_e} créée !")
            elif choix == "3":
                print("Lancement du Tournoi automatique ")

            elif choix == "4":
                print("/n--- CLASSEMENT GENERAL ---")
                joueurs = db.recuperer_tous_les_joueurs()
                for p, s in joueurs:
                    print(f"Pseudo: {p} | Score: {s}")

            elif choix == "5":
                print("Fermeture du programme ...")
                break
            else:
                print("Option invalide .")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    finally:
        db.fermer()
if __name__ == "__main__":
    main()        



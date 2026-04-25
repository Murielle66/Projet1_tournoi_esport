from entites import Organisatrice
from joueur import Joueur
from equipe import Equipe
from database import Database
from tournoi import Tournoi
def test_scenario_complet_tournoi():
    #Vérifie que tout le cycle de vie du tournoi fonctionne 
    db = Database(":memory:")  #Utilise une base en mémoire pour les tests
     #1. Création
    equipes = [Equipe(f"Team{i}") for i in range(4)]
    for i, eq in enumerate(equipes):
        j1 = Joueur(f"Nom{i}A", f"Pseudo{i}A")
        j2 = Joueur(f"Nom{i}B", f"Pseudo{i}B")
        eq.ajouter_joueur(j1)
        eq.ajouter_joueur(j2)
    #2. Logique du tournoi
    mon_tournoi = Tournoi("Test Cup",equipes)
    m1, m2 = mon_tournoi.generer_demies()
    #Validation
    assert len(m1.equipe1.liste_joueurs) == 2
    assert mon_tournoi.nom == "Test Cup"
    db.fermer()
    print(f"Test d'intégration réussi !")
if__name__ == "__main__": # type: ignore
test_scenario_complet_tournoi()
from entites import Organisatrice
from joueur import Joueur
from equipe import Equipe
from database import Database
from tournoi import Tournoi
def test_scenario_complet_tournoi():
    #Vérifie que tout le cycle de vie du tournoi fonctionne 
    db = Database(":memory:")  #Utilise une base en mémoire pour les tests
    print("\n--- DEBUT DU TEST D'INTEGRATION (8 EQUIPES)")
     #1. Création de 8 équipes avec deux joueurs chacun
    equipes = []
    for i in range(8):
       nom_equipe = f"Equipe_{i+1}"
       eq = Equipe(nom_equipe)
     #2. Création et ajout de deux joueurs  par équipes
       j1 = Joueur(f"Nom_{i}A", f"Pseudo_{i}A")
       j2 = Joueur(f"Nom_{i}B", f"Pseudo_{i}B")
       eq.ajouter_joueur(j1)
       eq.ajouter_joueur(j2)
       equipes.append(eq)
       db.sauvegarder_joueur(j1)
       db.sauvegarder_joueur(j2)
    #3. Création  du tournoi
    mon_tournoi = Tournoi("Test Cup",equipes)
   
   # 4. ÉTAPE 1 : QUARTS DE FINALE
    quarts = mon_tournoi.generer_quarts()
    gagnants_quarts = []
    for match in quarts:
        # On simule que l'équipe 1 gagne à chaque fois
      match.designer_vainqueur(match._equipe1.nom_equipe)
      gagnants_quarts.append(match.vainqueur)
    print(f"Liste des qualifiés : {gagnants_quarts}")
    assert len(gagnants_quarts) == 4
    print(">> Quarts de finale terminés : 4 vainqueurs qualifiés.")

    # 5. ÉTAPE 2 : DEMI-FINALES
    matchs_demi = mon_tournoi.generer_demies(gagnants_quarts)
    gagnants_demies = []
    for match in matchs_demi:
        match.designer_vainqueur(match._equipe1.nom_equipe)
        gagnants_demies.append(match.vainqueur)
    
    assert len(gagnants_demies) == 2
    print(">> Demi-finales terminées : 2 finalistes qualifiés.")

    # 6. ÉTAPE 3 : FINALE
    match_finale = mon_tournoi.lancer_finale(gagnants_demies[0], gagnants_demies[1])
    match_finale.designer_vainqueur(gagnants_demies[0].nom_equipe)
    
    print(f">> FINALE TERMINÉE. Vainqueur : {match_finale.vainqueur.nom_equipe}")
    assert match_finale.vainqueur == gagnants_demies[0]

    # 7. Nettoyage
    db.fermer()
    print("\n--- TEST D'INTÉGRATION RÉUSSI ---")

if __name__ == "__main__":
    test_scenario_complet_tournoi()
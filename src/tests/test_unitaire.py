import pytest
from  joueur import Joueur
from  equipe import Equipe
def test_creation_joueur_valide():
    #Vérifie qu'un joueur est bien créé .        
    j = Joueur("Kevin", "Zérion")
    assert j.pseudo == "Zérion"
    assert j.score_total == 0 
def test_score_negatif_impossible():
    #Vérifie que l'ajout des points négatifs lève une erreur ou est bloqué
    j = Joueur("Kevin", "Zérion")
    j.ajouter_points(-10)
    assert j.score_total == 0 
    # Le score ne doit pas avoir bougé 
def test_pseudo_vide():
    # Vérifie que le système refuse un pseudo vide.
    with pytest.raises(ValueError):
        Joueur("Kévin","")
    def test_ajout_joueur_equipe():
        # Vérifie la composition de l'équipe .
        equipe = Equipe("Titans")
        j = Joueur("Kevin", "Zérion")
        equipe.ajouter_joueur(j)
        assert len(equipe.liste_joueurs) == 1
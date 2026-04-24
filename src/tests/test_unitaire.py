import pytest
from  joueur import Joueur
from  equipe import Equipe
from tournoi import Tournoi
from entites import Organisatrice  
from entites import Personne
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
def test_tournoi_trop_peu_equipes():
    #Vérifie que le tournoi refuse moins de 4 équipes 
    with pytest.raises(ValueError):
        equipes_insuffisantes = [Equipe("Team A"), Equipe("Team B")]
        t = Tournoi("Fail Tournoi",equipes_insuffisantes)
        t.generer_demies() 
    def test_heritage_personne():
        # Vérifie que joueur et Organisatrice héritent correctement de personne
        j = Joueur ("Wazyr" ,"Zyro")
        admin = Organisatrice("Alex CARTER", "Admin")
         #Test :Le joueur a t'il bien un nom ? (attribut de personne)
        assert j.nom == "wazyr"
         #Test : L'admin est t'il bien considéré comme une instance de personne ?
        assert isinstance(admin, Personne)
        assert admin.nom == "Alex CARTER"
def test_modularite_composition():
     #Vérifie que lesmodules Equipe et Joueur collaborent sans erreur
     equipe = Equipe("Les Apex")
     joueur = Joueur(" Bob" ,"Genos")
     equipe.ajouter_joueur(joueur)
    
     #On vérifie que que l'objet dans la liste est bien l'objet d'origine
     assert equipe.ma_liste_joueurs[0].pseudo == "Genos"
     assert  equipe.liste_joueurs[0].nom == "Bob"   
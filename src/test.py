#Test encapsulation
from joueur import Joueur
def test_score_initial():
    j = Joueur("Zyro")
    assert j.obtenir_score() == 0

#Test Ajout des points 
    def test_ajout_points():
        j = Joueur("Keen")
        j.ajouter_points(10)
        assert j.obtenir_score() == 10

#Test equipe 
from equipe import Equipe 
from joueur import Joueur
def test_ajout_joueur():
    e = Equipe("Apex")
    j = Joueur("Zyro")
    e.ajouter_joueur(j)
    assert len(e.liste_joueurs) == 1

#Test match
from match import Match
from equipe import Equipe
def test_vainqueur_match():
    e1 = Equipe("Apex")
    e2 = Equipe("Nexus")
    m = Match(e1, e2)
    m.designer_vainqueur("Apex")
    assert m.vainqueur == e1


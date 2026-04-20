CAHIER DES CHARGES-ProjetPOO Python :Gestionnaire de Tournois
Binome: GUEDENON Murielle & AMOUSSA Rayane
Date : 20 avril 2026
Cours : Programmation avec Python/Informatique de Gestion

1. INTRODUCTION 
Ce projet consiste à crer une application en python capable de gérer un tournoi de jeux de A à Z. L'idée est de passer d'une gestion manuelle (souvent compliquée ) à une automatisation complète des matchs et des scores via un programme en ligne de commande.

2. Spécifications fonctionnelles
  2.1 Gestion des participants
  Le programme doit nous permettre de :
 • Enregistrer des joueurs avec leurs pseudos.
 • Créer des équipes et y ajouter des joueurs déjà créés.
 • Pouvoir afficher,modifier ou supprimer une équipe en cas d'erreur de saisie.
   2.2 Organisation du tournoi
  • Initialisation : on donne un nom au tournoi et on sélectionne les équipes participantes.
  • Brackets: Le programme doit générer automatiquement qui joue contre qui (Quarts,Demies,puis Finale).
  • Scores:Pour chaque match, on saisit le résulat. Le programme doit alors "qualifier" automatiquement le gagnant pour l'étape suivante.
  
  3. Choix Techniques
  Pour ce projet, on va respecter les contraintes suivantes :
 • Language : Python 3.10+
 • Méthode: Tout sera fait en POO (Programmation Orientée Objet). On va utiliser des classes pour bien séparer la logique(par exemple, un objet match recevra deux objets Equipe).
 • Stockage : On utilisera des dictionnaires et des listes pour garder les données en mémoire pendant l'exécution. 
 • L'utilisation de Git est obligatoire.
  
  4. Architecture des Classes
   1. Classe Joueur: Nom,pseudo,etc.
   2. Classe Equipe: Un nom et une liste d'objets Joueur.
   3. Classe Match: Prend deux équipes,gère le score et définit un vainqueur.
   4. Classe Tournoi: La classe "cerveau" qui contient la liste des matchs et l'arbre de progression.

   5. Environnement de travail
   On travaille sur Git pour ne pas perdre nos modifications et pouvoir fusionner nos codes. On utilise aussi un environnement virtuel (venv) pour que le projet soit propre.

  6. Organisation du binome
  Pour ce projet,nous allon travailler en collaboration sur Git,mais nous avons reparti les responsabilités principales pour gagner en efficacité:
  • Gestion des données: Murielle s'occupe en priorité de la structure des classes Joueur et Equipe et de l'interface de saisie.
  • Logique métier: Rayane se concentre sur l'algorithme de génération des matchs et la progression des scores.
  • Tests et Review: On prévoit de relire le code l'un de l'autre avant chaque commit important pour s'assurer que tout s'imbrique bien.


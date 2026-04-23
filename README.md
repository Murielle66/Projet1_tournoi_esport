CAHIER DES CHARGES-ProjetPOO Python : Gestionnaire de Tournois
Binôme : GUEDENON Murielle & AMOUSSA Rayane
Cours : Programmation avec Python/Informatique de Gestion


1. INTRODUCTION
Ce projet a pour but but de développer une application en Python permettant de gérer des tournois e-sport.
L’application doit simuler un système de compétition réel comme dans les jeux vidéo, où des joueurs ou des équipes s’affrontent jusqu’à la finale.
Le système permet notamment :
•	la création de tournois 
•	l’enregistrement de joueurs 
•	la constitution d’équipes 
•	la génération automatique de brackets (tableaux de matchs) 
•	le suivi des résultats jusqu’au vainqueur 
________________________________________
2. Fonctionnalités du système
🔹 Gestion des joueurs
Chaque joueur est identifié  par son nom et son pseudo .
Le système permet :
•	d’ajouter un joueur (pseudo , nom) 
•	de supprimer un joueur 
•	d’afficher la liste des joueurs 
•	de vérifier qu’un pseudo n’est pas déjà utilisé 
________________________________________
🔹 Gestion des équipes
Une équipe est un regroupement de joueurs.
Fonctionnalités :
•	créer une équipe avec un nom 
•	ajouter des joueurs dans une équipe 
•	retirer un joueur 
•	afficher les membres d’une équipe 
NB :  Une équipe est invalide si elle est vide.
________________________________________
🔹 Gestion des tournois
Un tournoi peut être :
•	solo : joueur contre joueur 
•	équipe : équipe contre équipe 
Le système permet :
•	créer un tournoi avec un nom 
•	choisir le type de tournoi 
•	ajouter les participants correspondants 
•	lancer le tournoi 
 NB : Un tournoi ne peut pas démarrer sans participants.
________________________________________
🔹 Génération des matchs (brackets)
Une fois le tournoi lancé :
•	les participants sont mélangés ou organisés 
•	des matchs sont générés automatiquement par paires 
•	les gagnants avancent au tour suivant 
•	le processus continue jusqu’à la finale 
👉 Exemple :
8 participants → 4 matchs → 2 demi-finales → 1 finale
________________________________________
3. Modélisation orientée objet (POO)
Le projet est structuré autour de classes avec des relations fortes.
________________________________________
🔸 Classe Joueur
Représente un participant individuel.
Attribut :
•	pseudo , nom .. 
👉 Le pseudo est l’identifiant principal du joueur dans tout le système.
________________________________________
🔸 Classe Equipe
Représente un groupe de joueurs.
Attributs :
•	nom de l’équipe 
•	liste de joueurs (Joueur) 
👉 Une équipe peut contenir plusieurs joueurs, stockés dans une liste Python.
________________________________________
🔸 Classe Match
Représente une confrontation entre deux participants.
Attributs :
•	participant 1 (joueur ou équipe) 
•	participant 2 (joueur ou équipe) 
•	score  
•	gagnant 
👉 Le gagnant est déterminé après simulation ou saisie du résultat.
________________________________________
🔸 Classe Tournoi
Classe principale qui orchestre tout le système.
Attributs :
•	nom du tournoi 
•	type (solo / équipe) 
•	liste des participants 
•	liste des matchs générés 
Rôle :
•	organiser les phases du tournoi 
•	générer les brackets 
•	gérer la progression des gagnants 
________________________________________
 4.  Relations entre les classes
•	Un joueur est défini  par son pseudo et son nom
•	Une équipe contient plusieurs joueurs 
•	Un match oppose deux participants 
•	Un tournoi contient plusieurs matchs et participants 
•	Les résultats des matchs déterminent l’évolution du tournoi 
👉 Ces relations permettent de simuler un tournoi complet de manière réaliste.
________________________________________
5.  Contraintes techniques
🔹 Gestion de version
•	utilisation obligatoire de Git 
•	dépôt sur GitHub ou GitLab 
•	commits réguliers avec messages clairs : 
o	ajout joueur 
o	création équipe 
o	génération bracket 
o	correction bugs 
________________________________________
🔹 Environnement de développement
•	utilisation d’un environnement virtuel (venv) 
•	gestion des dépendances via requirements.txt 
________________________________________
🔹 Norme de codage
•	respect strict de la norme PEP 8 
•	code structuré en plusieurs fichiers (modularité) 
•	noms de variables clairs et explicites 
________________________________________
🔹 Tests unitaires
•	utilisation de pytest 
•	tests sur les fonctions principales : 
o	création d’un joueur 
o	ajout/suppression dans une équipe 
o	génération des matchs 
o	détermination du gagnant 
👉 Objectif : garantir que chaque module fonctionne indépendamment.
________________________________________
6. Types de données utilisés
Le projet repose sur plusieurs types de structures :
•	listes : stockage des joueurs et équipes 
•	objets : représentation des entités (POO) 
•	chaînes de caractères : pseudos et noms 
•	booléens : validation des actions  

7. Organisation du binôme
  Pour ce projet, nous allons travailler en collaboration sur Git, mais nous avons reparti les responsabilités principales pour gagner en efficacité :
  • Gestion des données : Murielle s'occupe en priorité de la structure des classes Joueur et Equipe et de l'interface de saisie.
  • Logique métier : Rayane se concentre sur l'algorithme de génération des matchs et la progression des scores.
  • Tests et Review : On prévoit de relire le code l'un de l'autre avant chaque commit important pour s'assurer que tout s'imbrique bien.

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

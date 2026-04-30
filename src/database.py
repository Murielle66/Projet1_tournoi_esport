import sqlite3
class Database :
    # Gère la persistance des données du tournoi avec SQLite
    def __init__(self, db_name :str="tournoi.db"):
        # Initialisation de la Connexion et du curseur
        self._conn=sqlite3.connect(db_name)
        self._cursor=self._conn.cursor()
        self._creer_tables()
    def _creer_tables(self):
         #Creation la structure de la base de données 
         self._cursor.execute('''CREATE TABLE IF NOT EXISTS joueurs(
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             pseudo TEXT UNIQUE ,
                             score INTEGER DEFAULT 0
                             )
                             ''')
         self._conn.commit()

    def sauvegarder_joueur(self, joueur):
         # Sauvegarde ou met à jourun objet Joueur dans la base
      try:
         sql ='''
                             INSERT INTO joueurs
                             (pseudo, score) VALUES(? ,?)
                             ON CONFLICT(pseudo)DO
                             UPDATE SET score=excluded.score
                             ''' 
         self._cursor.execute(sql ,(joueur._pseudo, joueur._Joueur__score_total))
         self._conn.commit()
      except sqlite3.Error as e:
          print(f"Erreur Critique Base de Données :{e}")
   
    def recuperer_tous_les_joueurs(self):
         # Retourne la liste de tous les joueurs enregistrés
         self._cursor.execute("SELECT pseudo, score FROM joueurs")
         return self._cursor.fetchall() 
    
    def supprimer_joueur(self, pseudo):
         #Supprime un joueur définitivement de la base de données.
        query = "DELETE FROM joueurs WHERE pseudo = ?"
        self._cursor.execute(query, (pseudo,))
        self._conn.commit()

    def modifier_pseudo_joueur(self, ancien_pseudo, nouveau_pseudo):
        # Met à jour le pseudo d'un joueur en vérifiant s'il n'existe pas déjà.
        try:
            query = "UPDATE joueurs SET pseudo = ? WHERE pseudo = ?"
            self._cursor.execute(query, (nouveau_pseudo, ancien_pseudo))
            self._conn.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de la modification : {e}")
            return False
    
    def fermer(self):
         # Ferme la connexion à la base de données
         self._conn.close()
    
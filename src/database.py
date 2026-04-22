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
         sql ='''
                             INSERT INTO joueurs
                             (pseudo, score) VALUES(? ,?)
                             ON CONFLICT(pseudo)DO
                             UPDATE SET score=excluded.score
                             ''' 
         self._cursor.execute(sql ,(joueur._pseudo, joueur._Joueur__score_total))
         self._conn.commit()
   
    def recuperer_tous_les_joueurs(self):
         # Retourne la liste de tous les joueurs enregistrés
         self._cursor.execute("SELECT pseudo, score FROM joueurs")
         return self._cursor.fetchall() 
    
    def fermer(self):
         # Ferme propement la connexion à la base de données
         self._conn.close()
    
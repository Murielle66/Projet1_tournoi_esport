import sqlite3
class Database :
    def __init__(self, db_name="tournoi.db"):
        #Connexion automatique
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
        self.creer_tables()
    def creer_tables(self):
         #Creation des tables
         self.cursor.execute('''CREATE TABLE IF NOT EXISTS joueurs(
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             pseudo TEXT UNIQUE ,
                             score INTEGER DEFAULT 0
                             )
                             ''')
         self.conn.commit()

    def sauvegarder_joueur(self, joueur):
         # encapsulation du score
         self.cursor.execute('''
                             INSERT INTO joueurs
                             (pseudo, score) VALUES(? ,?)
                             ON CONFLICT(pseudo)DO
                             UPDATE SET score=excluded.score
                             ''' ,(joueur.pseudo, joueur.obtenir_score()))
         self.conn.commit()
    def fermer(self):
         self.conn.close()
    def recuperer_tous_les_joueurs(self):
         self.cursor.execute("SELECT pseudo, score FROM joueurs")
         return self.cursor.fetchall() #retourne une liste de tuples[(pseudo, score), . . .]
    
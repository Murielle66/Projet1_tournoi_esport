import tkinter as tk
from tkinter import messagebox, ttk
import random
from database import Database
from joueur import Joueur
from equipe import Equipe
from tournoi import Tournoi

class TournamentApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" E-Sport Manager ")
        self.root.geometry("1100x750")
        self.db = Database()
        
        # État de l'application
        self.equipes_selectionnees = []
        self.vainqueurs_quarts = []
        self.vainqueurs_demies = []
        self.matchs_quarts = [] # Pour fixer les matchs une fois générés

        # Style
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 10))

        # Layout principal
        self.menu_frame = tk.Frame(self.root, bg="#2c3e50", width=200)
        self.menu_frame.pack(side="left", fill="y")
        
        self.content_frame = tk.Frame(self.root, bg="white")
        self.content_frame.pack(side="right", expand=True, fill="both")

        self.setup_menu()
        self.afficher_classement()

    def setup_menu(self):
        tk.Label(self.menu_frame, text="MENU", fg="white", bg="#eb3a1b", font=("Arial", 14, "bold")).pack(pady=20)
        actions = [
            ("Classement / Joueurs", self.afficher_classement),
            ("Créer Équipe", self.afficher_creation_equipe),
            ("Lancer Tournoi", self.afficher_tournoi),
            ("Vider les Équipes", self.vider_donnees),
            ("Fermer", self.root.quit)
        ]
        for text, cmd in actions:
            btn = tk.Button(self.menu_frame, text=text, command=cmd, bg="#34495e", fg="white", 
                            relief="flat", height=2, font=("Arial", 10), activebackground="orange")
            btn.pack(fill="x", padx=10, pady=5)

    def nettoyer_cadre(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    #1. CLASSEMENT 
    def afficher_classement(self):
        self.nettoyer_cadre()
        tk.Label(self.content_frame, text="Classement des Joueurs", font=("Arial", 18), bg="white").pack(pady=10)
        tree = ttk.Treeview(self.content_frame, columns=("Pseudo", "Score"), show="headings")
        tree.heading("Pseudo", text="Pseudo"); tree.heading("Score", text="Score (Points)")
        tree.pack(pady=10, padx=20, fill="both", expand=True)
        for p, s in self.db.recuperer_tous_les_joueurs():
            tree.insert("", tk.END, values=(p, s))

            # Formulaire ajout 
        f = tk.LabelFrame(self.content_frame, text="Ajouter un nouveau joueur", bg="white")
        f.pack(pady=20, padx=20, fill="x")
        tk.Label(f, text="Pseudo:", bg="white").grid(row=0, column=0, padx=5)
        ent = tk.Entry(f)
        ent.grid(row=0, column=1, padx=5)
        
        def ajouter():
            if ent.get():
                self.db.sauvegarder_joueur(Joueur("Inconnu", ent.get()))
                self.afficher_classement()
            else: messagebox.showwarning("Erreur", "Pseudo vide !")
        
        tk.Button(f, text="Inscrire", command=ajouter, bg="#27ae60", fg="white").grid(row=0, column=2, padx=10)

    #2. CRÉER ÉQUIPE 
    def afficher_creation_equipe(self):
        self.nettoyer_cadre()
        tk.Label(self.content_frame, text="Formation des Équipes (2 joueurs/eq)", font=("Arial", 18), bg="white").pack(pady=10)
        lbl_status = tk.Label(self.content_frame, text=f"Équipes prêtes : {len(self.equipes_selectionnees)} / 8", fg="orange", bg="white")
        lbl_status.pack()
        listbox = tk.Listbox(self.content_frame, selectmode=tk.MULTIPLE, width=50)
        listbox.pack(pady=10)
        occupes = [j.pseudo for eq in self.equipes_selectionnees for j in eq.liste_joueurs]
        for p, s in self.db.recuperer_tous_les_joueurs():
            if p not in occupes: listbox.insert(tk.END, f"{p} ({s} pts)")
        ent_nom = tk.Entry(self.content_frame); ent_nom.insert(0, "Nom Équipe"); ent_nom.pack(pady=5)
        def valider():
            indices = listbox.curselection()
            if len(indices) == 2:
                eq = Equipe(ent_nom.get())
                for i in indices:
                    p = listbox.get(i).split(" (")[0]
                    eq.ajouter_joueur(Joueur("Inconnu", p))
                self.equipes_selectionnees.append(eq)
                self.afficher_creation_equipe()
            else: messagebox.showerror("Erreur", "Sélectionnez 2 joueurs !")
        tk.Button(self.content_frame, text="Enregistrer l'équipe", command=valider, bg="#2980b9", fg="white").pack(pady=10)

    #3. TOURNOI 
    def afficher_tournoi(self):
        if len(self.equipes_selectionnees) < 8:
            messagebox.showwarning("Incomplet", "Il faut 8 équipes pour lancer le tournoi !")
            return
        
        self.nettoyer_cadre()
        
        # Setup du Canvas avec Scrollbars
        container = tk.Frame(self.content_frame)
        container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(container, bg="#ecf0f1", highlightthickness=0)
        v_scroll = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        h_scroll = tk.Scrollbar(container, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        v_scroll.pack(side="right", fill="y")
        h_scroll.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.tournoi = Tournoi("Benin Championship", self.equipes_selectionnees)
        
        # Génération UNIQUE des matchs pour éviter les doublons au rafraîchissement
        if not self.matchs_quarts:
            self.matchs_quarts = self.tournoi.generer_quarts()

        self.dessiner_bracket()

    def dessiner_bracket(self):
        self.canvas.delete("all")
        
        # Affichage des Quarts
        for i, m in enumerate(self.matchs_quarts):
            self.creer_boite(50, 50 + (i*160), m, "QUART")
        
        # Affichage des Demies
        if len(self.vainqueurs_quarts) == 4:
            matchs_d = self.tournoi.generer_demies(self.vainqueurs_quarts)
            for i, m in enumerate(matchs_d):
                self.creer_boite(350, 130 + (i*320), m, "DEMIE")

        # Affichage Finale
        if len(self.vainqueurs_demies) == 2:
            m_f = self.tournoi.lancer_finale(self.vainqueurs_demies[0], self.vainqueurs_demies[1])
            self.creer_boite(650, 290, m_f, "FINALE")

        # Mise à jour de la zone de défilement
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def creer_boite(self, x, y, match, type_m):
        fill_c = "#90ee90" if match.vainqueur else "white"
        self.canvas.create_rectangle(x, y, x+180, y+80, fill=fill_c, width=2, outline="#2c3e50")
        self.canvas.create_text(x+90, y+40, text=f"{match._equipe1.nom_equipe}\nvs\n{match._equipe2.nom_equipe}", 
                                justify="center", font=("Arial", 10, "bold"))
        
        if not match.vainqueur:
           
            btn = tk.Button(self.canvas, text="Saisir Score", command=lambda: self.score_popup(match, type_m),
                            bg="orange", fg="white", font=("Arial", 8))
            self.canvas.create_window(x+90, y+100, window=btn)

    def score_popup(self, match, type_m):
        win = tk.Toplevel(self.root)
        win.title("Saisie du score")
        win.geometry("250x180")
        win.grab_set() # Bloque la fenêtre principale
        
        tk.Label(win, text=match._equipe1.nom_equipe).pack(pady=5)
        e1 = tk.Entry(win, justify="center"); e1.pack()
        tk.Label(win, text="VS").pack()
        e2 = tk.Entry(win, justify="center"); e2.pack()
        tk.Label(win, text=match._equipe2.nom_equipe).pack(pady=5)

        def ok():
            try:
                s1, s2 = int(e1.get()), int(e2.get())
                v = match._equipe1 if s1 > s2 else match._equipe2
                match.designer_vainqueur(v.nom_equipe)
                
                if type_m == "QUART" and v not in self.vainqueurs_quarts:
                    self.vainqueurs_quarts.append(v)
                elif type_m == "DEMIE" and v not in self.vainqueurs_demies:
                    self.vainqueurs_demies.append(v)
                elif type_m == "FINALE":
                    messagebox.showinfo("CHAMPION", f"Le vainqueur est {v.nom_equipe} !")
                
                win.destroy()
                self.dessiner_bracket()
            except ValueError:
                messagebox.showwarning("Erreur", "Veuillez entrer des scores valides.")
        
        tk.Button(win, text="Valider", command=ok, bg="#27ae60", fg="white").pack(pady=10)

    def vider_donnees(self):
        if messagebox.askyesno("Confirmation", "Réinitialiser le tournoi ?"):
            self.equipes_selectionnees = []
            self.vainqueurs_quarts = []
            self.vainqueurs_demies = []
            self.matchs_quarts = []
            self.afficher_classement()

if __name__ == "__main__":
    root = tk.Tk()
    app = TournamentApp(root)
    root.mainloop()
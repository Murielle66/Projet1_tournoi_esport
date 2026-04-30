import tkinter as tk
from tkinter import messagebox, ttk
from database import Database
from joueur import Joueur
from equipe import Equipe
from tournoi import Tournoi

class TournamentApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" E-Sport Manager ")
        self.root.geometry("1150x850")
        self.root.configure(bg="#1a1a1a")
        
        self.db = Database()
        self.equipes_selectionnees = []
        self.matchs_quarts = []
        self.vainqueurs_quarts = []
        self.vainqueurs_demies = []

        # Styles personnalisés
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#2d2d2d", foreground="white", fieldbackground="#2d2d2d", rowheight=35)
        self.style.map("Treeview", background=[('selected', 'orange')])
        self.style.configure("Treeview.Heading", background="#333333", foreground="orange", font=("Arial", 10, "bold"))

        #  Menu
        self.menu_frame = tk.Frame(self.root, bg="#0f0f0f", width=220)
        self.menu_frame.pack(side="left", fill="y")
        
        # Zone de contenu
        self.content_frame = tk.Frame(self.root, bg="#1a1a1a")
        self.content_frame.pack(side="right", expand=True, fill="both")

        self.setup_menu()
        self.afficher_classement()

    def setup_menu(self):
        tk.Label(self.menu_frame, text="ESPORT MANAGER", fg="orange", bg="#0f0f0f", font=("Impact", 20)).pack(pady=30)
        actions = [
            ("JOUEURS & SCORES", self.afficher_classement),
            ("GÉRER ÉQUIPES", self.afficher_creation_equipe),
            ("BRACKET LIVE", self.afficher_tournoi),
            ("RÉINITIALISER", self.vider_donnees)
        ]
        for text, cmd in actions:
            tk.Button(self.menu_frame, text=text, command=cmd, bg="#1a1a1a", fg="white", 
                      relief="flat", height=2, font=("Arial", 9, "bold"), activebackground="orange", cursor="hand2").pack(fill="x", padx=15, pady=8)

    def nettoyer_cadre(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    #  1: GESTION DES JOUEURS 
    def afficher_classement(self):
        self.nettoyer_cadre()
        tk.Label(self.content_frame, text="GESTION DES COMPÉTITEURS", font=("Arial", 18, "bold"), fg="white", bg="#1a1a1a").pack(pady=20)
        
        self.tree = ttk.Treeview(self.content_frame, columns=("Pseudo", "Points"), show="headings")
        self.tree.heading("Pseudo", text="PSEUDO DU JOUEUR")
        self.tree.heading("Points", text="POINTS CUMULÉS")
        self.tree.pack(pady=10, padx=40, fill="both", expand=True)
        self.rafraichir_joueurs()

        # Barre d'actions 
        btn_bar = tk.Frame(self.content_frame, bg="#1a1a1a")
        btn_bar.pack(fill="x", padx=40)
        tk.Button(btn_bar, text="MODIFIER PSEUDO", bg="#2980b9", fg="white", command=self.modifier_joueur_popup, font=("Arial", 9, "bold")).pack(side="left", padx=5)
        tk.Button(btn_bar, text="SUPPRIMER JOUEUR", bg="#c0392b", fg="white", command=self.supprimer_joueur_db, font=("Arial", 9, "bold")).pack(side="left", padx=5)

        # Formulaire d'ajout
        f_add = tk.LabelFrame(self.content_frame, text="Inscription nouveau joueur", bg="#1a1a1a", fg="orange", font=("Arial", 10, "bold"))
        f_add.pack(pady=30, padx=40, fill="x")
        self.ent_p = tk.Entry(f_add, bg="#2d2d2d", fg="white", insertbackground="white", font=("Arial", 12))
        self.ent_p.pack(side="left", padx=15, pady=15, expand=True, fill="x")
        tk.Button(f_add, text="ENREGISTRER", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), command=self.ajouter_j, padx=20).pack(side="right", padx=15)

    def rafraichir_joueurs(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        if not self.equipes_selectionnees:
         for p, s in self.db.recuperer_tous_les_joueurs():
            self.tree.insert("", tk.END, values=(p, s))
        else:
            for eq in self.equipes_selectionnees:
                self.tree.insert("", tk.END, values=(eq.nom_equipe, "Inscrite"))

    def ajouter_j(self):
        pseudo = self.ent_p.get().strip()
        if pseudo:
            self.db.sauvegarder_joueur(Joueur("Inconnu", pseudo))
            self.ent_p.delete(0, tk.END)
            self.rafraichir_joueurs()
        else: messagebox.showwarning("Attention", "Le pseudo est vide.")

    def supprimer_joueur_db(self):
        sel = self.tree.selection()
        if not sel: return
        pseudo = self.tree.item(sel[0])['values'][0]
        if messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer {pseudo} ?"):
            self.db.supprimer_joueur(pseudo)
            self.rafraichir_joueurs()

    def modifier_joueur_popup(self):
        sel = self.tree.selection()
        if not sel: return
        ancien = self.tree.item(sel[0])['values'][0]
        
        win = tk.Toplevel(self.root)
        win.title("Modifier")
        win.geometry("300x150")
        win.configure(bg="#0f0f0f")
        
        tk.Label(win, text=f"Nouveau pseudo pour {ancien}:", fg="white", bg="#0f0f0f").pack(pady=10)
        e = tk.Entry(win, justify="center")
        e.pack(); e.insert(0, ancien)
        
        def save():
            if self.db.modifier_pseudo_joueur(ancien, e.get()):
                win.destroy()
                self.rafraichir_joueurs()
            else: messagebox.showerror("Erreur", "Modification impossible.")
        tk.Button(win, text="METTRE À JOUR", bg="orange", command=save, font=("Arial", 9, "bold")).pack(pady=15)

    #  2: GÉRER ÉQUIPES 
    def afficher_creation_equipe(self):
        self.nettoyer_cadre()
        tk.Label(self.content_frame, text="FORMATION DES ÉQUIPES", font=("Arial", 18, "bold"), fg="white", bg="#1a1a1a").pack(pady=20)
        
        # Liste des duos
        f_eq = tk.LabelFrame(self.content_frame, text="Équipes engagées", bg="#1a1a1a", fg="orange")
        f_eq.pack(pady=10, padx=40, fill="both", expand=True)
        
        for eq in self.equipes_selectionnees:
            l = tk.Frame(f_eq, bg="#2d2d2d")
            l.pack(fill="x", pady=2, padx=5)
            tk.Label(l, text=f"{eq.nom_equipe.upper()} ({' & '.join([j.pseudo for j in eq.liste_joueurs])})", fg="white", bg="#2d2d2d").pack(side="left", padx=10)
            tk.Button(l, text="X", fg="#c0392b", bg="#2d2d2d", relief="flat", font=("Arial", 10, "bold"), command=lambda e=eq: self.del_eq(e)).pack(side="right", padx=5)

        # Création
        lb = tk.Listbox(self.content_frame, selectmode=tk.MULTIPLE, bg="#2d2d2d", fg="white", font=("Arial", 11))
        lb.pack(pady=10, padx=40, fill="x")
        occ = [j.pseudo for eq in self.equipes_selectionnees for j in eq.liste_joueurs]
        for p, s in self.db.recuperer_tous_les_joueurs():
            if p not in occ: lb.insert(tk.END, f"  {p}")
            
        en = tk.Entry(self.content_frame, justify="center", bg="#2d2d2d", fg="white", font=("Arial", 12))
        en.insert(0, "NOM ÉQUIPE"); en.pack(pady=5)

        def add_eq():
            idx = lb.curselection()
            if len(idx) == 2:
                eq = Equipe(en.get())
                for i in idx: eq.ajouter_joueur(Joueur("Inconnu", lb.get(i).strip()))
                self.equipes_selectionnees.append(eq)
                self.afficher_creation_equipe()
        tk.Button(self.content_frame, text="CRÉER DUO", bg="orange", font=("Arial", 10, "bold"), command=add_eq).pack(pady=15)

    def del_eq(self, eq):
        self.equipes_selectionnees.remove(eq)
        self.matchs_quarts = []
        self.afficher_creation_equipe()

    # 3: TOURNOI & SCROLL
    def afficher_tournoi(self):
        if len(self.equipes_selectionnees) < 8:
            messagebox.showwarning("Bracket", "Il faut 8 équipes pour générer le bracket."); return
        self.nettoyer_cadre()
        
        container = tk.Frame(self.content_frame, bg="#1a1a1a")
        container.pack(fill="both", expand=True)
        
        self.canvas = tk.Canvas(container, bg="#1a1a1a", highlightthickness=0)
        v_sc = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=v_sc.set)
        v_sc.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        if not self.matchs_quarts:
            self.tournoi = Tournoi("Benin Championship", self.equipes_selectionnees)
            self.matchs_quarts = self.tournoi.generer_quarts()
        self.dessiner_bracket()

    def dessiner_bracket(self):
        self.canvas.delete("all")
        # Titres
        self.canvas.create_text(140, 40, text="QUARTS", fill="orange", font=("Arial", 14, "bold"))
        self.canvas.create_text(440, 40, text="DEMIES", fill="orange", font=("Arial", 14, "bold"))
        self.canvas.create_text(740, 40, text="FINALE", fill="gold", font=("Arial", 16, "bold"))

        for i, m in enumerate(self.matchs_quarts):
            self.creer_boite(50, 80 + (i*160), m, "QUART")
        
        if len(self.vainqueurs_quarts) == 4:
            matchs_d = self.tournoi.generer_demies(self.vainqueurs_quarts)
            for i, m in enumerate(matchs_d): self.creer_boite(350, 160 + (i*320), m, "DEMIE")
            
        if len(self.vainqueurs_demies) == 2:
            m_f = self.tournoi.lancer_finale(self.vainqueurs_demies[0], self.vainqueurs_demies[1])
            self.creer_boite(650, 320, m_f, "FINALE")
        if m_f.vainqueur: 
            self.canvas.create_text(740, 450, text=f"VAINQUEUR: {m_f.vainqueur.upper()}", fill="gold", font=("Arial", 16, "bold"))
        
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def creer_boite(self, x, y, match, type_m):
        color = "orange" if match.vainqueur else "#2d2d2d"
        self.canvas.create_rectangle(x, y, x+180, y+80, fill=color, outline="orange", width=2)
        txt = f"{match._equipe1.nom_equipe.upper()}\nVS\n{match._equipe2.nom_equipe.upper()}"
        self.canvas.create_text(x+90, y+40, text=txt, fill="white" if not match.vainqueur else "black", font=("Arial", 9, "bold"), justify="center")
        
        if not match.vainqueur:
            btn = tk.Button(self.canvas, text="SCORE", bg="orange", font=("Arial", 8, "bold"), command=lambda: self.score_popup(match, type_m))
            self.canvas.create_window(x+90, y+100, window=btn)

    def score_popup(self, match, type_m):
        win = tk.Toplevel(self.root); win.geometry("250x200"); win.configure(bg="#0f0f0f"); win.grab_set()
        tk.Label(win, text=match._equipe1.nom_equipe, fg="white", bg="#0f0f0f").pack(pady=5)
        e1 = tk.Entry(win, justify="center"); e1.pack()
        tk.Label(win, text="CONTRE", fg="orange", bg="#0f0f0f").pack()
        e2 = tk.Entry(win, justify="center"); e2.pack()
        tk.Label(win, text=match._equipe2.nom_equipe, fg="white", bg="#0f0f0f").pack(pady=5)
        
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
                    messagebox.showinfo(" 🏆 CHAMPION 🏆 ", f"Félicitations à l'équipe {v.nom_equipe}!\nIls remportent le tournoi")    
                win.destroy();self.dessiner_bracket()
            except: pass
        tk.Button(win, text="VALIDER", bg="orange", font=("Arial", 10, "bold"), command=ok).pack(pady=10)

    def vider_donnees(self):
        if messagebox.askyesno("Reset", "Réinitialiser tout le tournoi ?"):
            self.equipes_selectionnees = []; self.matchs_quarts = []; self.vainqueurs_quarts = []; self.vainqueurs_demies = []
            self.afficher_classement()

if __name__ == "__main__":
    root = tk.Tk(); app = TournamentApp(root); root.mainloop()
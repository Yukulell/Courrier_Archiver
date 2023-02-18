# Importation des modules
import tkinter as tk
from tkinter import *
from tkinter import font as tkFont


# fonction
def close():
    # win.destroy()
    window.quit()


def creer_fenetre():
    def enregistrer_donnees():
        objet = champ_objet.get()
        date = champ_date.get()
        expediteur = champ_expediteur.get()

        with open("archive.txt", "a") as f:
            f.write(f"{objet}, {date}, {expediteur}\n")

        champ_objet.delete(0, tk.END)
        champ_date.delete(0, tk.END)
        champ_expediteur.delete(0, tk.END)

    fenetre = tk.Tk()
    fenetre.title("Ma fenêtre")
    fenetre.config(bg="#1f1f1f")
    helv12 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)

    label_objet = tk.Label(fenetre, text="Objet :", bg='#1f1f1f', fg='#ffffff', font=helv12)
    label_objet.grid(row=1, column=0)

    champ_objet = tk.Entry(fenetre, font=helv12)
    champ_objet.grid(row=1, column=1)

    label_date = tk.Label(fenetre, text="Date :", bg='#1f1f1f', fg='#ffffff', font=helv12)
    label_date.grid(row=2, column=0)

    champ_date = tk.Entry(fenetre, font=helv12)
    champ_date.grid(row=2, column=1)

    label_expediteur = tk.Label(fenetre, text="Expéditeur :", bg='#1f1f1f', fg='#ffffff', font=helv12)
    label_expediteur.grid(row=3, column=0)

    champ_expediteur = tk.Entry(fenetre, font=helv12)
    champ_expediteur.grid(row=3, column=1)

    bouton = tk.Button(fenetre, text="Envoyer", command=enregistrer_donnees, font=helv12)
    bouton.grid(row=4, column=0)


def creer_fenetre_recherche():
    def rechercher():
        objet = champ_objet.get()
        date = champ_date.get()
        expediteur = champ_expediteur.get()

        # Ouvrir le fichier
        try:
            with open("archive.txt", "r") as f:
                lignes = f.readlines()
        except FileNotFoundError:
            return

        # Rechercher les éléments
        resultats = []
        for ligne in lignes:
            elements = ligne.split(",")
            if (objet == "" or objet in elements[0]) and (date == "" or date in elements[1]) and (
                    expediteur == "" or expediteur in elements[2]):
                resultats.append(ligne)

        # Afficher les résultats dans une nouvelle fenêtre
        fenetre_resultats = Toplevel(fenetre)
        fenetre_resultats.title("Résultats de la recherche")
        fenetre_resultats.geometry("500x500")

        texte_resultats = Text(fenetre_resultats, height=20, width=60)
        texte_resultats.pack()

        if resultats:
            for resultat in resultats:
                texte_resultats.insert(END, resultat)
        else:
            texte_resultats.insert(END, "Aucun résultat trouvé.")
    fenetre = tk.Tk()
    fenetre.title("Rechercher dans l'archive")
    fenetre.config(bg="#1f1f1f")
    helv12 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)

    # Créer les champs d'objet, de date et d'expéditeur
    label_objet = tk.Label(fenetre, text="Objet :", font=helv12, bg='#1f1f1f', fg='#ffffff')
    label_objet.grid(row=1, column=0)
    champ_objet = tk.Entry(fenetre, font=helv12)
    champ_objet.grid(row=1, column=1)

    label_date = tk.Label(fenetre, text="Date :", font=helv12, bg='#1f1f1f', fg='#ffffff')
    label_date.grid(row=2, column=0)
    champ_date = tk.Entry(fenetre, font=helv12)
    champ_date.grid(row=2, column=1
                    )
    label_expediteur = tk.Label(fenetre, text="Expéditeur :", font=helv12, bg='#1f1f1f', fg='#ffffff')
    label_expediteur.grid(row=3, column=0)
    champ_expediteur = tk.Entry(fenetre, font=helv12)
    champ_expediteur.grid(row=3, column=1)

    # Créer le bouton pour effectuer la recherche
    bouton = tk.Button(fenetre, text="Rechercher", command=rechercher, font=helv12)
    bouton.grid(row=4, column=0)
    zone_texte = tk.Text(fenetre)


# Element en rapport avec la fenetre
window = Tk()
window.title("Archiveur de courrier")
window.config(bg="#1f1f1f")
window.geometry("640x480")
window.maxsize(640, 480)
window.minsize(640, 480)

# GUI
# Acceuil
helv36 = tkFont.Font(family='Helvetica', size=18, weight=tkFont.BOLD)
helv12 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
buton = Button(text="Ajouter un courrier", width=19, height=5, font=helv36, command=creer_fenetre)
buton.place(x=10, y=10)
buton = Button(text="Rechercher un courrier", width=19, height=5, font=helv36, command=creer_fenetre_recherche)
buton.place(x=335, y=10)
buton = Button(window, text="SORTIR", width=61, height=4, font=helv12, command=close)
buton.place(x=10, y=200)


# Boucle principale
if __name__ == "__main__":
    window.mainloop()

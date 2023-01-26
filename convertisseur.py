import tkinter as tk

#Variable qui convertit les type de monnaie

def convertir():
    montant = float(entree_montant.get())
    dev_depart = var1.get()
    dev_arrivee = var2.get()
    taux = taux_devises[dev_arrivee]/taux_devises[dev_depart]
    resultat = round(montant * taux, 2)
    entree_resultat.config(state='normal')
    entree_resultat.delete(0, tk.END)
    entree_resultat.insert(0, resultat)
    entree_resultat.config(state='readonly')
    history.append(f"{montant} {dev_depart} = {resultat} {dev_arrivee}")
    historique.insert(tk.END, history[-1])

#Variable pour effacer les entre de texte

def effacer_entre():
    entree_montant.delete(0, tk.END)
    entree_resultat.config(state='normal')
    entree_resultat.delete(0, tk.END)
    entree_resultat.config(state='readonly')

fenetre = tk.Tk()
fenetre.title("Convertisseur de devises")

#Valeurs des monnaie au moment ou ce code a etait fais

taux_devises = {"Euro": 1.0, "Dollar américain": 1.09,  "Yuan chinois": 7.35, "Yen": 141.70, "Livre sterling": 0.88}

var1 = tk.StringVar(value="Euro")
var2 = tk.StringVar(value="Dollar américain")

#Code pour les menu deroulant et les bouton

entree_montant = tk.Entry(fenetre)
entree_montant.grid(row=0, column=0, padx=5, pady=5)

label_depart = tk.Label(fenetre, text="De :")
label_depart.grid(row=1, column=0, padx=5, pady=5)

menu_depart = tk.OptionMenu(fenetre, var1, *taux_devises)
menu_depart.grid(row=1, column=1, padx=5, pady=5)

label_arrivee = tk.Label(fenetre, text="A :")
label_arrivee.grid(row=2, column=0, padx=5, pady=5)

menu_arrivee = tk.OptionMenu(fenetre, var2, *taux_devises)
menu_arrivee.grid(row=2, column=1, padx=5, pady=5) 

bouton_convertir = tk.Button(fenetre, text="Convertir", command=convertir)
bouton_convertir.grid(row=3, column=0, padx=5, pady=5)

bouton_clear = tk.Button(fenetre, text="Effacer", command=effacer_entre)
bouton_clear.grid(row=3, column=1, padx=5, pady=5)

label_resultat = tk.Label(fenetre, text="Résultat :")
label_resultat.grid(row=4, column=0, padx=5, pady=5)

entree_resultat = tk.Entry(fenetre)
entree_resultat.grid(row=4, column=1, padx=5, pady=5)
entree_resultat.config(state='readonly')

#Code pour l'historique

history = []
historique = tk.Listbox(fenetre, width=40)
historique.grid(row=5, column=0, padx=5, pady=5, columnspan=2, )

fenetre.mainloop()

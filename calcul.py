import tkinter as tk
from tkinter import ttk

fenetre=tk.Tk()
fenetre.geometry("800x800")
fenetre.title("LES UE DU SEMESTRE 1")

frm=ttk.Frame(fenetre)
frm.grid()

matieres = ["R101", "R102", "R103", "R104", "R105", "R106", "R107", "R108","R109", "R110", "R111", "R112", "R113", "R114", "R115","SAE11", "SAE12", "SAE13", "SAE14", "SAE15", "SAE16"]
les_resultat_saisie= []
for i, k in enumerate (matieres):
    matiere=ttk.Label(frm,text= k)
    matiere.grid(column=0,row=i, padx=20)
    
    saisie_des_notes=ttk.Entry(frm)
    les_resultat_saisie.append(saisie_des_notes)
    saisie_des_notes.grid(column=1,row=i)

    
def valid():
    les_note=[]
    for ind,champ in enumerate(les_resultat_saisie):
        note=  champ.get()
        les_note.append(note)

    des_note=[]
    for elt in les_note:
        des_note.append(float(elt))

    dict_des_notes= dict(zip(matieres,des_note))
    print(dict_des_notes)

    moyenne_ue1= ttk.Label(frm, text= f"la moyenen de ue1 est de {calcul_moy(ue1,dict_des_notes)}")
    moyenne_ue1.grid(column=1,row=22)
    moyenne_ue2= ttk.Label(frm, text= f"la moyenne de ue2 est de {calcul_moy(ue2,dict_des_notes)}")
    moyenne_ue2.grid(column=1,row=23)
    moyenne_ue3= ttk.Label(frm, text= f"la moyenne de ue3 est de {calcul_moy(ue3,dict_des_notes)}")
    moyenne_ue3.grid(column=1,row=24)


valider_final=ttk.Button(frm,text="valider",command=valid)
valider_final.grid(column=1,row=21)
    
fenetre.mainloop()
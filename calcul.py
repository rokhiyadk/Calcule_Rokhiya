import tkinter as tk #  pour créer une interface graphique
from tkinter import ttk # pour avoir des widgets 
import matplotlib.pyplot as plt # pour générer des graphiques
import numpy as np # matplotlib s'apuis sur c emodule pour fonctionner 
from PIL import Image,ImageTk # pour manipuler et afficher des images dans Tkinter

#fonction def saisie pour définir les coefficients et les notes 

def saisi_ue_coef():
    ue1={}
    ue2={}
    ue3={}
    k=["R101","R102","R103","R104","R105","R106","R107","R108","R109","R110","R111","R112","R113","R114","R115","SAE11","SAE12","SAE13","SAE14","SAE15","SAE16"]
    coef_ue1=[10,10,7,7,0,5,0,6,0,5,4,2,5,5,0,20,20,0,0,0,7]
    coef_ue2=[4,0,2,8,6,0,0,0,0,5,5,2,9,9,3,0,0,29,0,0,7]
    coef_ue3=[4,0,2,0,0,5,15,6,4,5,5,2,0,0,3,0,0,0,20,20,7]
    ue1= dict(zip(k,coef_ue1)) # on met dans un dictionnaire avec zip qui va lier chaque matiere a son coef 
    ue2= dict(zip(k,coef_ue2))
    ue3= dict(zip(k,coef_ue3))
    notes = {
        "R101": 14, "R102": 13, "R103": 12, "R104": 10, "R105": 11, "R106": 13,
        "R107": 15, "R108": 12, "R109": 14, "R110": 15, "R111": 14, "R112": 13,
        "R113": 12, "R114": 11, "R115": 10,
        "SAE11": 16, "SAE12": 15, "SAE13": 14, "SAE14": 13, "SAE15": 12, "SAE16": 15} # Dictionnaire contenant les notes initiales (valeurs par défaut)
    return ue1, ue2, ue3, notes 
    
saisi_ue_coef() 

ue1, ue2, ue3, notes = saisi_ue_coef() # pour recuperer les données retournées

# Cette fonction sert a calculer la moyenne general de chaque UE

def calcul_moy(coefs,note):
    total_note=0
    total_coef=0
    for matiere, coef in coefs.items(): # Parcourir toutes les matières et coefficients
        if coef > 0 and matiere in note:
            total_note += note[matiere] * coef
            total_coef += coef
        if total_coef == 0:
            return None
    return (total_note / total_coef) # calcule dans print de la moyenne ponderee 
    
calcul_moy(ue1,notes)

# Création de la fenêtre principale 

fenetre=tk.Tk()
fenetre.geometry("800x800")
fenetre.title("LES UE DU SEMESTRE 1")

# Creation d’un conteneur pour organiser les differents elements 

frm=ttk.Frame(fenetre) 
frm.grid()

matieres = ["R101", "R102", "R103", "R104", "R105", "R106", "R107", "R108","R109", "R110", "R111", "R112", "R113", "R114", "R115","SAE11", "SAE12", "SAE13", "SAE14", "SAE15", "SAE16"]
les_resultat_saisie= [] # Creation d'un dictionnaire vide pour stocker les zone de saisie

#Creation des labels et champs de saisie pour chaque matière 

for i, k in enumerate (matieres): 
    matiere=ttk.Label(frm,text= k)
    matiere.grid(column=0,row=i, padx=20)
    
    saisie_des_notes=ttk.Entry(frm) #  Zone de saisie pour entrer la note
    les_resultat_saisie.append(saisie_des_notes) # pour repurer la zone de saisie et le mettre dans le dictionnaire 
    saisie_des_notes.grid(column=1,row=i) # placement d echaque zonne de saisie au fur et a mesure (i)

# Fonction execute quand on clique sur "valider" on met une actiona notre bouton valid
def valid():
    les_note=[]
    for ind,champ in enumerate(les_resultat_saisie): # pour recuperer les valeurs saisies dans les champs
        notte=  champ.get()
        les_note.append(notte)

    des_note=[]
    for elt in les_note:
        des_note.append(float(elt)) # Conversion des notes en nombres float

    dict_des_notes= dict(zip(matieres,des_note)) # Prendre les notes et les mettre dans un dictionnaire avec leur matiere correspondnat 

    
    #Affichage des moyennes dans la fenêtre 
    
    moyenne_ue1= ttk.Label(frm, text= f"la moyenen de ue1 est de {calcul_moy(ue1,dict_des_notes)}") # on apelle la fonction calcul_moy definit precedement et on va calculer chaque ue avec les note saisie 
    moyenne_ue1.grid(column=3,row=2)
    moyenne_ue2= ttk.Label(frm, text= f"la moyenne de ue2 est de {calcul_moy(ue2,dict_des_notes)}")
    moyenne_ue2.grid(column=3,row=3)
    moyenne_ue3= ttk.Label(frm, text= f"la moyenne de ue3 est de {calcul_moy(ue3,dict_des_notes)}")
    moyenne_ue3.grid(column=3,row=4)
    
    # Pour recuperer des moyennes pour les afficher sur un graphique (oui je le fait 2x car y a eu un message d'erreur quand g mis une fois)
    
    moy_ue1= calcul_moy(ue1,dict_des_notes) 
    moy_ue2= calcul_moy(ue2,dict_des_notes) 
    moy_ue3= calcul_moy(ue3,dict_des_notes)

    
    #Création d’un diagramme en barres avec matplotlib 
    
    with plt.style.context("ggplot"):
            name= ["UE1","UE2","EU3"]
            values= [moy_ue1,moy_ue2,moy_ue3]
            plt.bar(name,values,color=['red','green','blue'])
            plt.savefig("diagramme.png") # Sauvegarde du graphique dans un fichier
            plt.close() # fermer la figure matplotlib apres l’avoir cree et sauvegarde
        
# Creation de mon bouton valider pour valider les saisies et calculer leur moyenne 

valider_final=ttk.Button(frm,text="valider",command=valid)
valider_final.grid(column=2,row=0)
canvas=tk.Canvas(frm,width=440,height=240) # Zone  pour afficher le graphique genere 
canvas.grid(column=5,row=21)

# Je fais une fonction affiche pour mettre une action a mon bouton affiche qui va me permettre d'afficher le graphique dans ma fenetre 
def affiche():
    
    img= Image.open("diagramme.png") # j'ouvre l'image
    img= img.resize((440,240)) # Redimensionne pour l’adapter au canvas
    photo=ImageTk.PhotoImage(img) # Conversion en image compatible Tkinter
    canvas.photo = photo # pour empecher la suppression de l’image
    canvas.create_image(0,0,image=photo,anchor="nw") # ancrage coin haut-gauche

# creationd e mon bouton affiche qui va me permettre d'fficher l'image
valider_image= ttk.Button(frm,text="Afficher le diagramme",command=affiche)
valider_image.grid(column=3,row=15)




    
fenetre.mainloop() # garder la fenetre ouverte
    

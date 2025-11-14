def saisi_ue_coef():
    ue1={}
    ue2={}
    ue3={}
    k=["R101","R102","R103","R104","R105","R106","R107","R108","R109","R110","R111","R112","R113","R114","R115","SAE11","SAE12","SAE13","SAE14","SAE15","SAE16"]
    coef_ue1=[10,10,7,7,0,5,0,6,0,5,4,2,5,5,0,20,20,0,0,0,7]
    coef_ue2=[4,0,2,8,6,0,0,0,0,5,5,2,9,9,3,0,0,29,0,0,7]
    coef_ue3=[4,0,2,0,0,5,15,6,4,5,5,2,0,0,3,0,0,0,20,20,7]
    ue1= dict(zip(k,coef_ue1))
    ue2= dict(zip(k,coef_ue2))
    ue3= dict(zip(k,coef_ue3))
    notes = {
        "R101": 14, "R102": 13, "R103": 12, "R104": 10, "R105": 11, "R106": 13,
        "R107": 15, "R108": 12, "R109": 14, "R110": 15, "R111": 14, "R112": 13,
        "R113": 12, "R114": 11, "R115": 10,
        "SAE11": 16, "SAE12": 15, "SAE13": 14, "SAE14": 13, "SAE15": 12, "SAE16": 15}
    return ue1, ue2, ue3, notes
    
saisi_ue_coef()

ue1, ue2, ue3, notes = saisi_ue_coef()

def calcul_moy (coefs,note):
    total_note=0
    total_coef=0
    for matiere, coef in coefs.items():
        if coef > 0 and matiere in notes:
            total_note += notes[matiere] * coef
            total_coef += coef
        if total_coef == 0:
            return None
    return (total_note / total_coef)

moyenne_ue1= calcul_moy(ue1,notes)
moyenne_ue2= calcul_moy(ue2,notes)
moyenne_ue3= calcul_moy(ue3,notes)

print(f'la moyenne de ue1 est de {moyenne_ue1} au 1er semestre')
print(f'la moyenne de ue2 est de {moyenne_ue2} au 1er semestre')
print(f'la moyenne de ue3 est de {moyenne_ue3} au 1er semestre')
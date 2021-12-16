#Variables et dictionnaires
from typing import Match


Chargetotal=0
Dic_Charge = {
    "Contribution pour le Remboursement de la Dette Sociale et Contribution Sociale Généralisee imposable" : 3.49,
    "Contribution Sociale Généralisee non imposable" : 6.15,
    "Assurance maladie" : 0.95,
    "Assurance vieillesse" : 8.44,
    "Assurance chomage" : 3.05,
    "Retraite complementaire (IRCEM)" : 3.81,
    "Cotisation AGFF":1.02
}

#Prise de renseignement
print("Nom ?")
nom=input()
print("Prenom")
prenom=input()
print("Nombre d'enfant ?")
nbr_enfant=int(input())
print("Combien d'heure de travail ?")
nbr_heure=int(input())
print("Statut ?\n\t1)Cadre\n\t2)Agent de maitrise\n\t3)Employé de bureau\n\t")
statut=int(input())

print("\n\n\n\nNom : ",nom,"\nPrenom : ",prenom)
#Calcul du taux horaires
if statut == 1:
    tauxh=3
elif statut == 2:
    tauxh=10
elif statut== 3:
    tauxh=1

#Calcul majoration du taux horaire en cas d'heure sup
if nbr_heure in range (170,180):
    tauxh+=tauxh*0.5
    print("\n",nbr_heure," heures Majoration de 50%")
elif nbr_heure > 180:
    tauxh+=tauxh*0.60
    print(nbr_heure," heures Majoration de 60%")
else:
    print(nbr_heure," heures Pas de majoration")

#Calcul des charges
SalaireBrut = tauxh*nbr_heure
print("Salaire brut = ",SalaireBrut," euros\n")
for i,j in Dic_Charge.items():
    Charge=SalaireBrut*j
    Charge /= 100
    print(int(Charge),'euros\t',i)
    Chargetotal+=Charge

#Calul Prime Enfant.
if nbr_enfant == 0:
    prime = 0
elif nbr_enfant == 1:
    prime = 20
elif nbr_enfant == 2:
    prime = 50
else:
    bonus=nbr_enfant-2
    bonus*=20
    prime=bonus+70

#calcul du salaire net
Salairenet=SalaireBrut-Chargetotal+prime
print("\n\nSalaire net\tSalaire brut\t-\tCharge total\tprime")
print(Salairenet," euros \t",SalaireBrut," euros\t","-\t",int(Chargetotal)," euros\t",prime," euros")

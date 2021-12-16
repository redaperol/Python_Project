dic_chec = {}
lowest=9999999
highest =0
nbrinf200=0
totalinf200=0
totalsup200=0
nbrsup200=0
print("Bonjour bienvenue sur C.H.E.C.KOTRON")
while True:
    print("Numero du cheque ?")
    num=int(input())
    if num == 0:
        break
    else:
        print("Montant du cheque ?")
        montant=int(input())
        #on cherche la valeur la plus basse et plus haute
        dic_chec[num] = montant
        if montant < lowest:
            lowest = montant
        if montant > highest:
            highest = montant
        
#calcul basiques
Nbr_chek=len(dic_chec)
montant_total=sum(dic_chec.values())
moy=montant_total/Nbr_chek

#calcul des cheques superieurs et inferieurs a 200
for i in dic_chec:
    if dic_chec[i] < 200:
        nbrinf200+=1
        totalinf200+=dic_chec[i]
    if dic_chec[i] > 200:
        nbrsup200+=1
        totalsup200+=dic_chec[i]

#Determine les numeros de cheques les plus haut et les plus bas
for i, j in dic_chec.items():
    if lowest == j:
        lowestnum=i
    if highest == j:
        highestnum=i

#Affichage des resultats
print("\n\nnombre de cheque = ",Nbr_chek)
print("montant total = ", montant_total)
print("Moyenne = ", moy)
print("\n\nNombre de cheque inferieur a 200 ",nbrinf200,",Valeur total des cheques = ",totalinf200)
print("Nombre de cheque superieur a 200 ",nbrsup200,",Valeur total des cheques = ",totalsup200)
print("\n\nMontant le plus petit =\t",lowest,"\nNumero du cheque :\t",lowestnum)
print("\n\nMontant le plus grand =\t",highest,"\nNumero du cheque :\t",highestnum)
print("fin du programe")
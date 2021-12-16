prix_boisson_abs=60
prix_boisson=prix_boisson_abs/100
argent=0
argent_abs=0
piece=0
rendu=0
dic_piece={
    200:0,
    100:0,
    50:0,
    20:0,
    10:0,
    5:0
}

def monnaie(i,j):
    for a in dic_piece:
        if i >= a and dic_piece[a] >0:
            i-=a
            dic_piece[a]-=1
            j+=a
    return(i,j)
while True:
    print("______________________________________")
    print("Bienvenue !")
    print("______________________________________")

    while True:
        print("Le prix d'un cafe est de : ",'{:.2f}'.format(prix_boisson))
        print("Votre credit est de ", '{:.2f}'.format(argent))
        print("piece accepte : 2€, 1€, 0.50€, 0.20€, 0.10€, 0.05€")
        print("\nInserer une piece !")
        piece=int(100*float(input()))
    
    #ajout de la piece dans l'inventaire
        for a in dic_piece:
            if piece == a:
                dic_piece[a]+=1
                argent_abs+=piece
            else:
                print("piece non reconnu, desole")

    #credit tout pile
        if argent_abs == prix_boisson_abs:
            print("Merci ! Voila votre cafe")
            break
    
    #credit superieur au prix on rend la monnaie
        elif argent_abs > prix_boisson_abs:
            argent_abs-=prix_boisson_abs
            while argent >0:
                change,k=monnaie(argent,j)
                rendu+=k
                if change == argent:
                    print("Desole la machine n'a plus de piece nous ne pouvons pas vous rendre la monnaie")
                    print("voici votre monnaie",'{:.2f}'.format(rendu))
                    break
                else:
                    argent=change
            print("voici votre monnaie",'{:.2f}'.format(rendu))
    #pas assez de credit
        else:
            argent= argent_abs/100
print("fin du programme")
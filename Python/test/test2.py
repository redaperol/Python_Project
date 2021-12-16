dic_piece={
    200:1,
    100:3,
    50:0,
    20:2,
    10:0,
    5:1
}
argent=int(input("argent ?"))

def monnaie(i,j):
    for a in dic_piece:
        if i >= a and dic_piece[a] >0:
            i-=a
            dic_piece[a]-=1
            j+=a
    return(i,j)

rendu=0
while argent >0:
    a,b=monnaie(argent,rendu)
    rendu+=b
    if a == argent:
        print("Desole la machine n'a plus de piece nous ne pouvons pas vous rendre la monnaie")
        break
    else:
        argent=a
    print("monnaie",b)
    #print(argent)

for a in dic_piece:
    print(a,"\t",dic_piece[a])


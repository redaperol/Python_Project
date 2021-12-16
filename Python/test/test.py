Chargetotal=0
DicCharge = {
    "COT_SAL" : 3.49,
    "COT_CSGNI" : 6.15,
    "COT_ASSMALADIE" : 0.95,
    "COT_ASS_VIEL" : 8.44,
    "COT_ASS_CHOM" : 3.05,
    "COT_IRCEM" : 3.81,
    "COT_AGFF":1.02
}
SalaireBrut =451
for i,j in DicCharge.items():
    Charge=SalaireBrut*j
    Charge /= 100
    print('charge',i,Charge,'euros')
    Chargetotal+=Charge
print (Chargetotal)
Prime=[2,3]
PrimeTest=False
limite=1000000
counter=2
test=4
temp=[]

def PrimeFinder(a,b,c):
    for i in a:
        r=b%i
        if r==0:
            c=False
            return(a,b,c)
    c=True
    return(a,b,c)

while test < limite:#counter<1000:#
    Prime,test,PrimeTest=PrimeFinder(Prime,test,PrimeTest)
    #print("test : ",test)
    #print("primetest : ",PrimeTest)
    #print("counter : ",counter)
    if PrimeTest == True:
        Prime.append(test)
        counter+=1
        for i in PrimeTest:
            res=test*i
            if res >limite:
                break
            temp.append(res)
    test+=1
print(Prime[-1])

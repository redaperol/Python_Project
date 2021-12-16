def test(a,b,c):
    a+=1
    b+=2
    c+=3
    return (a,b,c)

testa=1
testb=2
testc=3
testa,testb,testc=test(testa,testb,testc)
print("testa :",testa)
print("testb :",testb)
print("testc :",testc)
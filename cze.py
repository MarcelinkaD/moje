import math 

a,b,c,d = map(int,input().split())

def czyMiesci(sprC, sprD, bokA, bokB):
    if((sprC <= bokA and sprD <= bokB) or (sprD <= bokA and sprC <= bokB)):
        return True

dzielnikiC = []
dzielnikiD = []



for i in range(1,int(math.sqrt(c)) +2):

    if(c % i == 0):        
        drugiDzielnik = c/i
        dzielnikiC.append(i)
        dzielnikiC.append(drugiDzielnik)


for i in range(1,int(math.sqrt(d)) +2):

    if(d % i == 0):        
        drugiDzielnik = d/i 
        dzielnikiD.append(i)
        dzielnikiD.append(drugiDzielnik)


cd = c*d
for mdc in dzielnikiC:
    for mdd in dzielnikiD:
        if(czyMiesci(mdc*mdd, cd/ (mdc*mdd), a, b)):
            print("TAK")
            quit()


print("NIE")

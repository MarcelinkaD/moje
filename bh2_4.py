#okazuje sie ze to "problem" hamminga
def main():
    h=[]        
    h.append(1)
    n=int(input())
    i = j = k = 0
    ostatni = h[0]
    while n > 0:
        print(ostatni, end = " ")
        
        while h[i]*2<=ostatni:
            i+=1
            
        while h[j]*3<=ostatni:
            j+=1
            
        while h[k]*5<=ostatni:
            k+=1
            
        ostatni = min(h[i]*2,h[j]*3,h[k]*5)
        h.append(ostatni)        
        n-=1
        
main()

from sys import stdin
from collections import Counter
input = stdin.readline

def main():
    liczba_slow = int(input())
    tab = []
    w = 0
    naj = 0
    slowa = []
    
    for i in range(liczba_slow):
        slowo = str(input())
        #spacja = ''
        #slownik = {}
        
#         for k in slowo.strip():
#             if k != "\n":
#                 if(k in slownik):
#                     slownik[k] += 1
#                 else:
#                     slownik[k] = 1
        slo_strip = slowo.strip()
        
        tab.append(Counter(slo_strip))
        slowa.append(len(slo_strip))
        
        for k in range(i ,-1,-1):
            if k != i:
                if tab[i] == tab[k]:
                    w += 1
                    naj = max(naj, slowa[i])            
            

#     for i in range(len(tab)):
#         for k in range(i, len(tab)):
#             if k != i:
#                 if tab[i] == tab[k]:
#                     w += 1
#                     naj = max(naj, len(slowa[i]))
                
    print(str(w) + " " + str(naj))
    #print(w)
    
main()
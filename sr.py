from sys import stdin
import bisect
input = stdin.readline

def main():
    ile_razy_zakupiono, ludzie_w_wagonie, szukany_wagon = map(int, input().split())
    system_dobry = {}
    
    for i in range(ile_razy_zakupiono):
        num_wag, os = map(int, input().split())
        
        if num_wag in system_dobry:
            if system_dobry[num_wag] + os <= ludzie_w_wagonie:
                system_dobry[num_wag] += os
        else:
            if os < ludzie_w_wagonie:
                system_dobry[num_wag] = os
            else:
                system_dobry[num_wag] = 0
            
    print(len(system_dobry))
    #system_dobry.keys()
    
    for i in sorted(system_dobry):
        print(i, system_dobry[i])
    
    maksik = max(system_dobry)
    
    if maksik < szukany_wagon:
        print(maksik, system_dobry[maksik])
    else:
        klucze = sorted(system_dobry.keys())
        spr = bisect.bisect_left(klucze, szukany_wagon)
        print(klucze[spr], system_dobry[klucze[spr]])
        

    
main()
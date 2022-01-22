def main():
    liczba_kolegow = int(input())
    plot = str(input())
    
    pref_nie = [0] * (len(plot) + 7)
    pref_ziel = [0] * (len(plot) + 7)
    
    for indeks in range(1, len(plot) + 1):
        if(plot[indeks - 1] == "n"):
            pref_nie[indeks] = 1 + pref_nie[indeks - 1]
        else:
            pref_nie[indeks] = pref_nie[indeks - 1]
            
        if(plot[indeks- 1] == "z"):
            pref_ziel[indeks] = 1 + pref_ziel[indeks - 1]
        else:
            pref_ziel[indeks] = pref_ziel[indeks - 1]
    
    for i in range(liczba_kolegow):
        od, do = map(int, input().split())
        
        #od -= 1
        #do -= 1
        nie = pref_nie[do] - pref_nie[od - 1]
        ziel = pref_ziel[do] - pref_ziel[od - 1]
        
        if(nie > ziel):
            print("n " + str(nie - ziel))
        elif(ziel > nie):
            print("z " + str(ziel - nie))
        else:
            print("labor omnia vincit")
main()
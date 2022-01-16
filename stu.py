def MAIN():
    dziuple, liczba_par = map(int, input().split())
    wierzcholek = [[] for i in range(dziuple + 1)]
    
    for para in range(liczba_par):
        ten_pierwszy, ten_drugi = map(int, input().split())
        wierzcholek[ten_pierwszy].append(ten_drugi)
        wierzcholek[ten_drugi].append(ten_pierwszy)
        
    for i in range(1, len(wierzcholek)):
        wierzcholek[i].sort()
    
    for i in range(1, len(wierzcholek)):
        if(len(wierzcholek[i]) == 0):
            print("Wiewior sam!")
        else:    
            for j in range(len(wierzcholek[i])):
                print(wierzcholek[i][j], end = " ")
            print("")
    
MAIN()

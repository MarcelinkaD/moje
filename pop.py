from sys import stdin
input = stdin.readline

def MAIN():
    uzytkownicy, liczba_par, min_popularnosc = map(int, input().split())
    wchodzace = [set() for i in range(uzytkownicy + 1)]
    wychodzace = [set() for i in range(uzytkownicy + 1)]    
    stopien_popularnosci_wierzcholka = [0] * (uzytkownicy + 1)
    
    for para in range(liczba_par):
        watcher, cool_ziomek = map(int, input().split())
        wchodzace[cool_ziomek].add(watcher)
        wychodzace[watcher].add(cool_ziomek)
        
    for i in range(1, uzytkownicy + 1):
        if(len(wchodzace[i]) >= min_popularnosc):    
            for k in wychodzace[i]:
                stopien_popularnosci_wierzcholka[k] += 1
       
    ilosc_zapytan = int(input())
    
    for i in range(ilosc_zapytan):
        ktos = int(input())
        
        print(stopien_popularnosci_wierzcholka[ktos])
    
MAIN()
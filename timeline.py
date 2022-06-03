from sys import stdin
input = stdin.readline

def main():
    wejscie = open("timeline.in", "r")
    wyjscie = open("timeline.out", "w")
    
    
    liczba_czynnosci, liczba_dni, liczba_zaleznosci = map(int, wejscie.readline().split())
    czynnosci = [0] + list(map(int, wejscie.readline().split()))
    graf = [[] for i in range(liczba_czynnosci + 1)]
    stopien = [0] * (liczba_czynnosci + 1)
    
    for i in range(liczba_zaleznosci):
        pierwsza, druga, dni = map(int, wejscie.readline().split())
        graf[pierwsza].append([druga, dni])
        stopien[druga] += 1
    
    gotowe = []
    for i in range(1, liczba_czynnosci + 1):
        if (stopien[i] == 0):
            gotowe.append(i)
    
    while (len(gotowe) > 0):
        v = gotowe[-1]
        gotowe.pop()
        for u, x in graf[v]:
            stopien[u] -= 1
            if (stopien[u] == 0):
                gotowe.append(u)
                
            czynnosci[u] = max(czynnosci[u], czynnosci[v] + x)

    for v in range(1, liczba_czynnosci + 1):
        wyjscie.write(str(czynnosci[v]) + "\n")
        
main()
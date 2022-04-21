from sys import stdin
input = stdin.readline

def main():
    liczba_wie, liczba_par = map(int, input().split())
    graf = [[] for i in range(liczba_wie + 1)]
    ile_wchodzi = [0] * (liczba_wie + 1)
    gotowe = []
    kolejnosc = []
    
    for i in range(1,liczba_par + 1):
        przed, po = map(int, input().split())
        graf[przed].append(po)
        ile_wchodzi[po] += 1
        
    for i in range(1, liczba_wie + 1):
        if ile_wchodzi[i] == 0:
            gotowe.append(i)
    
    while len(gotowe) != 0:
        i = gotowe.pop()
        kolejnosc.append(i)
        for k in range(len(graf[i])):
            u = graf[i][k]
            ile_wchodzi[u] -= 1
            if ile_wchodzi[u] == 0:
                gotowe.append(u)
    
    if len(kolejnosc) != liczba_wie:
        print("IMPOSSIBLE")
    else:
        for a in kolejnosc:
            print(str(a), end = " ")
        print("\n")
    
main()
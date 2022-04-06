from sys import stdin
input = stdin.readline

def main():
    napis = str(input())
    napis = " " + napis.strip()
    max_wyniki = [0] * len(napis)
    akt_wynik = 0
    czer = 0
    nie = 0
    koraliki = [0] * len(napis)
    
    for i in range(len(napis)):
        if napis[i] == "C":
            koraliki[i] = 1
        else:
            koraliki[i] = -1
            
    for i in range(3, len(napis)):
        akt_wynik = max(koraliki[i] + koraliki[i - 1] + koraliki[i - 2] + max_wyniki[i - 3], max_wyniki[i - 1])
        max_wyniki[i] = akt_wynik
        
    print(max_wyniki[len(koraliki) - 1])
    
main()
# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/has/

from sys import stdin
input = stdin.readline

def oblicz(akt):
    pie_i_ost = {}
        
    for i in range(len(akt)):
        if akt[i] not in pie_i_ost:
            pie_i_ost[akt[i]] = []
            pie_i_ost[akt[i]].append(i)
            pie_i_ost[akt[i]].append(i)
        else:
            pie_i_ost[akt[i]][1] = i
                
    w = 0
    
    for i in pie_i_ost:
        w += pie_i_ost[i][1] - pie_i_ost[i][0]
        
    return w

def gen(literki, akt):
    if not literki:
        return akt
    
    max_w = -1
    wynik = []
    
    for i in range(len(literki)):
        s, wynik = gen(literki[:i] + literki[i + 1 : len(literki)], akt + [literki[i]])
        obl_s = oblicz(akt)
        
        if obl_s > max_w:
            max_w = obl_s
            wynik = s
        
    return (max_w, wynik)

def main():
    ile_mamy = list(map(int, input().split()))
    l = []
    alfa = []
    n = 0
    literki = []
    
    for i in range(26):
        n += ile_mamy[i]
        
        for _ in range(ile_mamy[i]):
            literki.append((chr(i + 97)))
    
    for i in range(97, 97 + 26):
        alfa.append(str(chr(i)))
        
    print(gen(literki, []))
    
main()
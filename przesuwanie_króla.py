# https://szkopul.edu.pl/problemset/problem/oVHtxvef7lm-fuSKDBo79BkB/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    od = str(input().strip())
    do = str(input().strip())
    literki = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}
    odw_literki = {1 : "a", 2 : "b", 3 : "c", 4 : "d", 5 : "e", 6 : "f", 7 : "g", 8 : "h"}
    w = []
    
    akt_lit, akt_licz = od[0], int(od[1])
    kon_lit, kon_licz = do[0], int(do[1])
    
    while akt_lit != kon_lit or akt_licz != kon_licz:
        if literki[akt_lit] < literki[kon_lit]:
            if akt_licz < kon_licz:
                akt_licz += 1
                akt_lit = odw_literki[literki[akt_lit] + 1]
                w.append("NE")
            elif akt_licz > kon_licz:
                akt_licz -= 1
                akt_lit = odw_literki[literki[akt_lit] + 1]
                w.append("SE")
            else:
                akt_lit = odw_literki[literki[akt_lit] + 1]
                w.append("E")
        elif literki[akt_lit] > literki[kon_lit]:
            if akt_licz < kon_licz:
                akt_licz += 1
                akt_lit = odw_literki[literki[akt_lit] - 1]
                w.append("NW")
            elif akt_licz > kon_licz:
                akt_licz -= 1
                akt_lit = odw_literki[literki[akt_lit] - 1]
                w.append("SW")
            else:
                akt_lit = odw_literki[literki[akt_lit] - 1]
                w.append("W")
        else:
            if akt_licz < kon_licz:
                akt_licz += 1
                w.append("N")
            elif akt_licz > kon_licz:
                akt_licz -= 1
                w.append("S")
                
    print(len(w))
    for i in w:
        print(i, end = " ")
        
main()
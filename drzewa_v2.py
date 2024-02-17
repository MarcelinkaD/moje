# https://szkopul.edu.pl/problemset/problem/h7P1F1yz9gBplZVMII4a442e/site/?key=statement

from sys import stdin
input = stdin.readline

def czy_mozna(ost, i, n):
    if ost != i - 1 and i != 0 and i + 1 != n:
        return True
    return False

def znajdz(literki, l, n, ile_ma, l2):
    a, b = 0, 0
    ktora = 0
    akt_sum = l[0]
    ost = -1e18
    
    for i in range(1, n):
        if akt_sum == ile_ma and l2[i] == literki[ktora]:
            if czy_mozna(ost, i, n):
                if ktora == 0:
                    a = i + 1
                    ktora = 1
                    ost = i
                else:
                    b = i + 1
                    return (a, b)
                akt_sum = 0
            else:
                akt_sum += l[i]
        else:
            akt_sum += l[i]
        
    return ("BRAK", "")
        

def main():
    n = int(input())
    l = str(input().strip())
    suma = 0
    a, b = "BRAK", ""
    liczby = [0 for _ in range(n)]
    
    for i in range(n):
        if l[i] == "J":
            suma += 1
            liczby[i] = 1
        else:
            liczby[i] = -1
            suma -= 1
            
    if suma % 3 == 0:
        a1, b1 = znajdz("JS", liczby, n, suma // 3, l)
        a2, b2 = znajdz("SJ", liczby, n, suma // 3, l)
        
        if a1 != "BRAK":
            if a2 != "BRAK":
                if a1 < a2 and a1 != 0:
                    a, b = a1, b1
                elif a1 > a2 and a2 != 0:
                    a, b = a2, b2
                else:
                    if b1 < b2 and b1 != 0:
                        a, b = a1, b1
                    else:
                        a, b = a2, b2
            else:
                a, b = a1, b1
        else:
            if a2 != "BRAK":
                a, b = a2, b2
            else:
                a, b = "BRAK", ""
        
    else:
        if (suma - 2) % 3 == 0:
            a, b = znajdz("JJ", liczby, n, (suma - 2) // 3, l)
        if (suma + 2) % 3 == 0:
            a, b = znajdz("SS", liczby, n, (suma + 2) // 3, l)
                    
    print(a, b)
            
main()
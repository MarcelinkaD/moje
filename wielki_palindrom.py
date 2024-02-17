# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r4b/

from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    pol = n // 2
    srodek = ""
    liczby = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    akt_i_licz = 0
    pol_nap = ""
    w = ""
    
    if (n <= k and n != 1) or k > len(liczby):
        print("NIE")
        return
    
    for i in range(n):
        if i < pol:
            pol_nap += liczby[akt_i_licz]
            akt_i_licz += 1
        elif i == pol and n % 2 == 1:
            srodek = liczby[akt_i_licz]
            akt_i_licz += 1
        else:
            break
        
        if akt_i_licz == k:
            akt_i_licz = 0
    
    w = pol_nap + srodek + pol_nap[::-1]    
    
    for i in range(k - 1, n):
        odc = w[(i + 1) - k : i + 1]
        sett = set(odc)
        
        if len(sett) != len(odc):
            print("NIE")
            return
        
    print(w)
    
main()
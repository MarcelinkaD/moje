# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r0b/

from sys import stdin
input = stdin.readline

def main():
    n, q = map(int, input().split())
    wynik = [0 for _ in range(n)]
    ile_zostalo = n
    akt = 0
    
    for _ in range(q):
        litera, k = map(str, input().split())
        k = int(k)
        
        if litera == "Z":
            akt += k / ile_zostalo
        else:
            wynik[k - 1] = round(akt, 5)
            ile_zostalo -= 1
        
    for i in wynik:
        print(i, end = " ")
    
main()
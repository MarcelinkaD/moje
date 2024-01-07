# https://szkopul.edu.pl/c/testowy_dd/p/zam/

from sys import stdin
input = stdin.readline

def main():
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    ile_do_konca = [0 for _ in range(n + 1)]
    ile_do_konca[n] = l[-1]
    
    for i in range(n - 1, 0, -1):
         ile_do_konca[i] = ile_do_konca[i + 1] + l[i - 1]
         
    for i in range(1, n + 1):
        dla_potwora = ile_do_konca[i] / 20
        dla_bajtka = ile_do_konca[i] / 10
        
        ile_do_konca[i] = (dla_potwora, dla_bajtka)
        
    for _ in range(q):
        p, b = map(int, input().split())
        
        if p >= b:
            print("NIE")
        else:
            if ile_do_konca[p][0] < ile_do_konca[b][1]:
                print("NIE")
            else:
                print("TAK")
    
main()
# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/par/

from sys import stdin
input = stdin.readline

def main():
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    l.insert(0, 0)
    ile_zero = [0 for _  in range(n + 1)]
    ile_jeden = [0 for _  in range(n + 1)]
    ile_0_przed_1 = [0 for _  in range(n + 1)]
    
    for i in range(1, n + 1):
        ile_zero[i] = ile_zero[i - 1]
        ile_jeden[i] = ile_jeden[i - 1]
        ile_0_przed_1[i] = ile_0_przed_1[i - 1]
        
        if l[i] == 0:
            ile_zero[i] += 1
        else:
            ile_jeden[i] += 1
            ile_0_przed_1[i] += ile_zero[i]
                
    for _ in range(q):
        od, do = map(int, input().split())
        bledny_wyn = ile_0_przed_1[do] - ile_0_przed_1[od - 1]
        ile_zero_wczesniej = ile_zero[od - 1]
        ile_jeden_teraz = ile_jeden[do] - ile_jeden[od - 1]
        
        print(bledny_wyn - (ile_zero_wczesniej * ile_jeden_teraz))
    
main()
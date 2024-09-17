# https://szkopul.edu.pl/c/marcelina-domin/p/mon/

from sys import stdin
input = stdin.readline

def inRange(x, n):
    if x < n and x > -1:
        return True
    return False

def main():
    n = int(input())
    l = list(map(int, input().split()))
    max_wyn = 0
    ile_par_od_i = [0 for _ in range(n)]
    
    for i in range(n):
        if inRange(i - 1, n):
            ile_par_od_i[i] = ile_par_od_i[i - 1]
            if l[i - 1] == l[i]:
                ile_par_od_i[i] += 1
                
    for i in range(n):
        if inRange(i + 1, n) and inRange(i - 1, n):
            if l[i] == l[i + 1]:
                if l[i - 1] == l[i]:
                    nowy_wyn = ile_par_od_i[-1] - 2
                else:
                    nowy_wyn = ile_par_od_i[-1]
            else:
                if l[i - 1] == l[i]:
                    nowy_wyn = ile_par_od_i[-1]
                else:
                    nowy_wyn = ile_par_od_i[-1] + 2
                
        elif inRange(i + 1, n):
            if l[i] == l[i + 1]:
                nowy_wyn = ile_par_od_i[-1] - 1
            else:
                nowy_wyn = ile_par_od_i[-1] + 1
        else:
            if l[i] == l[i - 1]:
                nowy_wyn = ile_par_od_i[-1] - 1
            else:
                nowy_wyn = ile_par_od_i[-1] + 1
            
        max_wyn = max(max_wyn, nowy_wyn)  
        
    print(max_wyn)
        
    
main()
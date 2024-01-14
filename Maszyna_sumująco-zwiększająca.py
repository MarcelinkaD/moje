# https://solve.edu.pl/contest/root-wsi-divstart-s40/problem/1542/view

from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    ile = 0
    suma = 0
    
    for _ in range(q):
        s = str(input().strip())
        
        if len(s) == 3:
            print(suma)
        else:
            a, b = s.split()
            if a == "INSERT":
                ile += 1
                suma += int(b)
            else:
                suma += ile * int(b)
    
main()
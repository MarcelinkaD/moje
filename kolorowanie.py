# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/kol/

from sys import stdin
input = stdin.readline    

def main():
    MOD = 1000000007
    n = int(input())
    s = str(input().strip())
    
    if n == 1:
        w = 3
    elif n == 2:
        w = 9
    else:
        w = (n // 3) * 9

    print(w % MOD)
            
main()
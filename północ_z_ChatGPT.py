# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r1b/

from sys import stdin
input = stdin.readline
        
def main():
    q = int(input())
    w = ()
    ile = 10000000
    
    for _ in range(q):
        godz, minu = map(int, input().split())
        ile_min = 0

        if godz == 12:
            ile_min += minu
        else:
            ile_min += godz * 60
            ile_min += minu
            
        if ile_min < ile:
            ile = ile_min
            w = (godz, minu)
            
    print(w[0], w[1])
            
            
main()
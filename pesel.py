# https://pl.spoj.com/problems/JPESEL/

from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    
    for _ in range(q):
        s = str(input().strip())
        w = (int(s[0]) * 1) + (int(s[1]) * 3) + (int(s[2]) * 7) + (int(s[3]) * 9) + (int(s[4]) * 1) + (int(s[5]) * 3) + (int(s[6]) * 7) + (int(s[7]) * 9) + (int(s[8]) * 1) + (int(s[9]) * 3) + (int(s[10]) * 1)
        nw = str(w)
        
        if nw[-1] == "0":
            print("D")
        else:
            print("N")
        
main()
    
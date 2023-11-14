# https://sio2.mimuw.edu.pl/c/oij18-1/p/oij/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    s = str(input().strip())
    o = 0
    i = 0
    j = 0
    
    for k in s:
        if k == "O":
            o += 1
        elif k == "I":
            i += o
        else:
            j += i
            
    print(j == n)
    
main()
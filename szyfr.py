# https://szkopul.edu.pl/c/testowy_dd/p/scz/25252/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n, lit = map(str, input().split())
    n = int(n)
    s = str(input().strip())
    c1 = C(s)
    ta_najw = ""
    maxi = -1
    
    for key in c1:
        if c1[key] > maxi:
            maxi = c1[key]
            ta_najw = key
            
    roznica = ord(lit) - ord(ta_najw)

    for i in s:
        ile = ord(i) + roznica
        if ile > 64 and ile < 91:
            w = ile
        elif ile < 91:
            temp = 64 - ile
            w = 90 - temp
        else:
            temp = ile - 91
            w = 65 + temp
        
        
        print(chr(w), end = "")
            
    
main()
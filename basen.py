from sys import stdin
input = stdin.readline

def obl_pole(ai, aw, bi, bw):
    bok1 = bi - ai
    bok2 = min(aw, bw)
    
    return bok1 * bok2
    

def main():
    n = int(input())
    l = list(map(int, input().split()))
    lewo = 0
    prawo = n - 1
    max_wyn = 0
    
    while lewo < prawo:
        max_wyn = max(max_wyn, obl_pole(lewo, l[lewo], prawo, l[prawo]))
        
        if l[lewo] < l[prawo]:
            lewo += 1
        elif l[prawo] < l[lewo]:
            prawo -= 1
        else:
            lewo += 1
            
    print(max_wyn)
    
main()


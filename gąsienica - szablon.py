from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    glowa = -1
    ogon = 0
    akt_wyn = 0
    max_wyn = -1
    
    while ogon < n - 1:
        while glowa < n - 1 and (spelania sie warunek):
            glowa += 1
            akt_wyn += l[glowa]
            max_wyn = max(akt_wyn, max_wyn)
            
        akt_wyn -= l[ogon]
        ogon += 1
        max_wyn = max(akt_wyn, max_wyn)
    
    print(max_wyn)
    
main()

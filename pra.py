from sys import stdin
input = stdin.readline

def main():
    liczba_kolesi = int(input())
    poczatki = []
    konce = []
    g = 0
    ba = 0
    
    for i in range(liczba_kolesi):
        a, b = map(int, input().split())
        g += a
        poczatki.append(a)
        konce.append(b)
        
    g //= liczba_kolesi
    
    for i in poczatki:
        if i != g:
            ba += abs(i - g)
            
    print(g, ba)
    
main()
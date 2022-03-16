from sys import stdin
input = stdin.readline

def main():
    liczba_sam = int(input())
    samochody = list(map(int, input().split()))
    wynik = 0
    w_prawo = 0
    
    for i in range(liczba_sam):
        if samochody[i] == 0:
            w_prawo += 1
        else:
            wynik += w_prawo
            
    print(wynik)
    
main()
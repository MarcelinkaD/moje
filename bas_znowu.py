from sys import stdin
input = stdin.readline

def main():
    liczba_basenow = int(input())
    baseny = list(map(int, input().split()))
    wysokosc_i = 0
    wysokosc_k = 0
    min_wys = 0
    pole = 0
    max_pole = 0
    
    for i in range(liczba_basenow):
        wysokosc_i = baseny[i]
        for k in range(i + 1, liczba_basenow):
            wysokosc_k = baseny[k]
            min_wys = min(wysokosc_i, wysokosc_k)
            pole = (k - i) * min_wys
            max_pole = max(max_pole, pole)
            
    print(max_pole)
    
main()
from sys import stdin
input = stdin.readline

def main():
    liczba_mew, dzielnik = map(int, input().split())
    mewy = list(map(int, input().split()))
    reszty = set([])
    
    for i in range(liczba_mew):
        reszty.add(mewy[i] % dzielnik)
        
    reszty = list(reszty)
    
    reszty.sort()
    
    for i in reszty:
        print(i, end = " ")
        
main()
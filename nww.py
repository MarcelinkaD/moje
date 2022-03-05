from sys import stdin
input = stdin.readline

def NWD(n, k):
    x = 0
    while k != 0:
        x = n % k
        n, k = k, x
        
    return n
    
def NWW(n, k):
    return n * k // NWD(n, k)
    
def main():
    liczba_liczb = int(input())
    
    for i in range(liczba_liczb):
        c, b = map(int, input().split())
        print(NWW(c, b))

main()
from itertools import permutations

def main():
    k = int(input())
    cyfry = list(map(int, input().split()))
    wszystkie_kombinacje = [''.join(map(str, p)) for p in permutations(cyfry)]
    wszystkie_liczby = list(set([int(k) for k in wszystkie_kombinacje]))
    wszystkie_liczby.sort()
    
    for i in wszystkie_liczby:
        if i % k == 0:
            print(i)
    
main()
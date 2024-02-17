# https://szkopul.edu.pl/c/testowy_dd/p/tab/24193/

from itertools import accumulate as ac
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    tab1 = list(map(int, input().split()))
    tab2 = list(map(int, input().split()))
    pref1, pref2 = list(ac(tab1)), list(ac(tab2))
    
    for i in range(n):
        
    
main()
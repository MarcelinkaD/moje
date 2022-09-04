from sys import stdin
input = stdin.readline
from itertools import accumulate

def main():
    n = int(input())
    wisnie = map(int, input().split())
    pref1 = list(accumulate(wisnie))
    pref1.insert(0, 0) 
    liczbaPytan = int(input())
    
    for pytanie in range(liczbaPytan):
        od, do = map(int, input().split())
        print(pref1[do] - pref1[od - 1])

main()

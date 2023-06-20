# https://leetcode.com/problems/count-primes/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    if n == 0 or n == 1 or n == 2:
        return 0

    n -= 1
    sito = [0, 1] * (n//2) + [1]
    sito[1], sito[2] = 0, 1
        
    for i in range(3, int(n**0.5+1), 2):
        if sito[i] == 1:
            sito[i*i::2*i] = [0] * int((n+2*i-1-i*i)/(2*i))

    pref = [0 for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        pref[i] = pref[i - 1] + sito[i]

    print(pref[-1])
main()
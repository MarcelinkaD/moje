# https://szkopul.edu.pl/problemset/problem/b9z7CefMu8uwRXaCBm9FiUyO/site/?key=statement

import math
from sys import stdin
input = stdin.readline

def main():
    x = str(input().strip())
    jaka_potega = 10 ** len(x)
    x = int(x)
    jaka_potega -= 1
    d = math.gcd(x, jaka_potega)
    x //= d
    jaka_potega //= d
    
    print(str(x) + "/" + str(jaka_potega))
    
main()
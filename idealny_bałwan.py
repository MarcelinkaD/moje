# https://sio2.mimuw.edu.pl/c/oij18-1/p/bal/

from sys import stdin
input = stdin.readline

def czy_da_sie(r, limit):
    r2, r3 = 2 * r, 3 * r
    v = (r ** 2) + (r2 ** 2) + (r3 ** 2)
    return v <= limit

def main():
    limit = int(input())
    start, stop = 1, limit
    max_r = -1
    
    while start < stop:
        r = (start + stop) // 2
        if czy_da_sie(r, limit):
            max_r = max(r, max_r)
            start = r + 1
        else:
            stop = r
            
    h = 12 * max_r
    
    print(h)
    
main()
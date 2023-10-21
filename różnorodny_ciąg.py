# https://sio2.mimuw.edu.pl/c/oij18-1/p/cia/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    zlicz = [0 for _ in range(l[-1] + 1)]
    w = 0
    
    for i in l:
        zlicz[i] += 1
        
    for i in range(len(zlicz) -1, 0, -1):
        if zlicz[i] > 1:
            do_przeniesienia = zlicz[i] - 1
            zlicz[i] -= do_przeniesienia
            zlicz[i - 1] += do_przeniesienia
            w += do_przeniesienia
            
    print(w)
    
main()
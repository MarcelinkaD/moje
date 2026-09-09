from sys import stdin
from math import sqrt
input = stdin.readline

def main():
    l = [i for i in range(1, 11)]
    print(l)
    print()
    
    l1 = l[3::2]
    print(l1)
    
    l2 = l[::-2]
    print(l2)
    
    l3 = l[8::-2]
    print(l3)
    
    l4 = l[:8:2]
    print(l4)
    
    l5 = l[2:8:2]
    print(l5)
    
    l6 = l[::2]
    print(l6)
    
main()
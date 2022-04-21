from sys import stdin
import math
input = stdin.readline

def main():
    n = int(input())
    c = False
    
    if n == 1:
        return "NIE"
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "NIE"
        
    return "TAK"
    
print(main())
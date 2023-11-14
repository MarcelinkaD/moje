import math

def czy_pierwsza(N):
    if N == 0 or N == 1:
        return False
    
    do = int(math.sqrt(N)) + 1
    
    for i in range(2, do):
        if N % i == 0:
            return False
        
    return True

N = int(input())

print(czy_pierwsza(N))
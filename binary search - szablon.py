import bisect as b
from sys import stdin
input = stdin.readline

def binary_git_kolejnosc(li, n):
    bi = b.bisect_left(li, n)
    if bi != len(li) and li[bi] == n:
        return bi
    else:
        return -1
    
def binary_nie_git_kolejnosc(li, n):
    pocz = 0
    kon = len(li) - 1
    
    while pocz <= kon:
        srodek = (pocz + kon) // 2
        
        if li[srodek] < n:
            kon = srodek
        elif li[srodek] > n:
            pocz = srodek + 1
        else:
            return srodek
    
    return pocz    


def main():
    n, k = map(int, input().split())
    co = str(input().strip())
    l = list(map(int, input().split()))

    if co == "mal":
        print(binary_nie_git_kolejnosc(l, k))
    else:
        print(binary_git_kolejnosc(l, k))
    
    
main()

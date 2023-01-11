from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    zap = []
    maxi = -1
    
    for _ in range(q):
        a, b = map(int, input().split())
        zap.append([a, b])
        maxi = max(maxi, a)
    
    szcze = [0] * (maxi + 1)
    szcze[1] = 1
    szcze[2] = 2
    szcze[3] = 3
    
    for i in range(4, maxi + 1):
        szcze[i] = szcze[i - 1] + szcze[i - 2]
        
    for i in zap:
        print(szcze[i[0]] % (2 ** i[1]))
    
main()
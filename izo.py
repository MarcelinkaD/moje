from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = [int(input()) for _ in range(n)]
    w = sum(l)
    l.sort()
    
    for i in range(n // 2):
        w += l[n - i - 1] - l[i]
            
    print(w)
    
main()
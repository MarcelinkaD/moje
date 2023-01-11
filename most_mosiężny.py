from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    a = []
    w = [0] * n
    
    for _ in range(n):
        a.append(int(input()))
        
    w[0] = a[0]
    
    if n == 1:
        print(w[0])
        return 0
    
    w[1] = a[0] + a[1]
                    
    for i in range(2, n):
        pom = max(w[i - 1], w[i - 2] + a[i])
        w[i] = max(pom, w[i - 3] + a[i - 1] + a[i])
        
    print(max(w))
    
main()
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    k = n // 2
    w = n
    
    if n == 1:
        print(1)
    else:
        for i in range(1, k):
            if k - i > 0:
                w += k - i
            else:
                break
                
        print(w - 1)
        
main()
from sys import stdin
input = stdin.readline

def main():
    n, k = map(int,input().split())
    nowe_n = n
    str_n = str(n)
    
    for i in range(k):
        str_n = str(nowe_n)
        ost_n = str_n[len(str_n) - 1]
        if ost_n == "0":
            nowe_n //= 10
        else:
            nowe_n -= 1
            
            
    print(nowe_n)
            
main()
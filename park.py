# https://szkopul.edu.pl/c/testowy_dd/p/par/24151/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    w = [[-1, -1] for _ in range(n)]
    mnl = -1
    mnp = -1
    l = []
    
    for k in range(n):
        i = int(input())
        if i > mnl:
            mnl = i
        
        w[k][0] = mnl
        l.append(i)
        
    for i in range(n - 1, -1, -1):
        if l[i] > mnp:
            mnp = l[i]
        
        w[i][1] = mnp
        
    for i in w:
        print(i[0], i[1])
    
main()
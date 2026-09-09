from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(str, input().split()))
    zlicz = dict()
    
    for i in l:
        lit = i[0]
        if lit not in zlicz:
            zlicz[lit] = 0
        
        
    
main()
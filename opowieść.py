# https://szkopul.edu.pl/problemset/problem/dSJo19HkxZw1_5ThjwFNiKp6/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    s = str(input())
    czy_jest = set()
    w = 0
    
    for i in range(n):
        lit = s[i]
        if lit.isupper():
            if lit.lower() not in czy_jest:
                czy_jest.add(lit)
            else:
                w += 1
                czy_jest.add(lit)
        else:
            if lit.upper() not in czy_jest:
                czy_jest.add(lit)
            else:
                w += 1
                czy_jest.add(lit)
                
    print(w)
        
    
main()
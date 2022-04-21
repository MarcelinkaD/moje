from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    g = 1
    
    if n <= 1:
        print(1)
    else:
        for i in range(1, n + 1):
            g *= i
            if g > 10:
                g = int(str(g)[len(str(g)) - 1])
            
        g = str(g)
        
        print(g[len(g) - 1])
    
main()
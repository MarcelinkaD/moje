from sys import stdin
input = stdin.readline

def main():
    MAXN = int(1e5 + 7)
    sito = [True for _ in range(MAXN)]
    sito[0], sito[1] = False, False
    
    for i in range(2, MAXN):
        if sito[i]:
            for k in range(i + i, MAXN, i):
                sito[k] = False
                
    q = int(input())
    
    for _ in range(q):
        n = int(input())
        
        print(sito[n])
    
main()
from sys import stdin
input = stdin.readline

def main():
    a, b = map(str, input().split())
    wynik = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                wynik[i][j] = wynik[i - 1][j - 1] + 1
            else:
                wynik[i][j] = max(wynik[i - 1][j], wynik[i][j - 1])
                
    print(wynik[len(a)][len(b)])      
    
    
main()
    
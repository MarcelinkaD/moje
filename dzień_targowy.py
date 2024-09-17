# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/dzi/

from sys import stdin
input = stdin.readline

def main():
    m, n = map(int, input().split())
    l = [[] for _ in range(m)]
    
    for k in range(m):
        wiersz = str(input().strip())
        
        for i in range(n):
            if wiersz[i] == "0":
                l[k].append(0)
            else:
                l[k].append(1)
        
    sumy = [[0 for _ in range(n)] for _ in range(m)]
    sumy_zero = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        if i == 0:
            sumy[0][0] = l[0][0]
            for k in range(1, n):
                sumy[i][k] = sumy[i][k - 1] + l[i][k]
        else:
            for k in range(n):
                if k == 0:
                    sumy[i][k] = l[i][k] + sumy[i - 1][k]
                else:
                    sumy[i][k] = (sumy[i - 1][k] + sumy[i][k - 1]) - sumy[i - 1][k - 1] + l[i][k]
        if i == 0:
            if l[0][0] == 0:
                sumy_zero[0][0] = 1
            for k in range(1, n):
                if l[i][k] == 0:
                    sumy_zero[i][k] = sumy_zero[i][k - 1] + 1
                else:
                    sumy_zero[i][k] = sumy_zero[i][k - 1]
        else:
            for k in range(n):
                if k == 0:
                    if l[i][k] == 0:
                        sumy_zero[i][k] = 1 + sumy_zero[i - 1][k]
                    else:
                        sumy_zero[i][k] = sumy_zero[i - 1][k]
                else:
                    if l[i][k] == 0:
                        sumy_zero[i][k] = (sumy_zero[i - 1][k] + sumy_zero[i][k - 1]) - sumy_zero[i - 1][k - 1] + 1
                    else:
                        sumy_zero[i][k] = (sumy_zero[i - 1][k] + sumy_zero[i][k - 1]) - sumy_zero[i - 1][k - 1]
            
    max_w = -1e18
    
    for i in range(m):
        for k in range(n):
            if l[i][k] == 0:
                continue
            for j in range(i, m):
                for c in range(k, n):
                    if l[j][c] == 0:
                        break
                    if i == 0:
                        if k == 0:
                            ile_zer = sumy_zero[j][c]
                            if ile_zer == 0:
                                max_w = max(max_w, sumy[j][c])
                        else:
                            ile_zer = sumy_zero[j][c] - sumy_zero[j][k - 1]
                            if ile_zer == 0:
                                max_w = max(max_w, sumy[j][c] - sumy[j][k - 1])
                    elif k == 0:
                        ile_zer = sumy_zero[j][c] - sumy_zero[i - 1][c]
                        if ile_zer == 0:
                            max_w = max(max_w, sumy[j][c] - sumy[i - 1][c])
                    else:
                        ile_zer = sumy_zero[j][c] - sumy_zero[j][k - 1] - sumy_zero[i - 1][c] + sumy_zero[i - 1][k - 1]
                        if ile_zer == 0:
                            max_w = max(max_w, sumy[j][c] - sumy[j][k - 1] - sumy[i - 1][c] + sumy[i - 1][k - 1])
                    
    print(max_w)
    
main()
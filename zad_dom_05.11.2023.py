n = int(input())
l = list(map(int, input().split()))
w = 0
MAXI = int(1e3)
dodatnik = 0
poprzedni = l[0]
i = 1

while i < n:
    aktualny = l[i]
    
    if aktualny + dodatnik <= poprzedni:
        dodatnik += MAXI
        w += 1
        
    poprzedni = aktualny + dodatnik
    i += 1
    
print(w)
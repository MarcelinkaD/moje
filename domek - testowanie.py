def fast(n, m, l):
    l = []
    
    for _ in range(n):
        i = str(input().strip())
        li = []
        
        for k in i:
            li.append(k)
        
        l.append(li)
        
    for j in range(m):
        gdzie = n - 2
        for i in range(n - 1, -1, -1):
            if l[i][j] == "*":
                if l[i + 1][j] == "#":
                    gdzie -= 1
                    continue
            
                l[gdzie][j] = "*"
                l[i][j] = "."
                gdzie -= 1
            elif l[i][j] == "#":
                gdzie = i - 1
                
    return l
        
    
def brut(n, m, picture):
    picture = [list(row) for row in picture]
    
    for col in range(m):
        for row in range(n - 2, -1, -1): 
            if picture[row][col] == '*':
                while row < n - 1 and picture[row + 1][col] == '.':
                    picture[row][col], picture[row + 1][col] = picture[row + 1][col], picture[row][col]
                    row += 1
                
    return [''.join(row) for row in picture]
        
        
import random

numer_testu = 1
while True:
    n = random.randint(3, 100)
    m = random.randint(1, 100)
    a = []
    
    for i in range(n - 1):
        s = ""
        for _ in range(m):
            k = random.randint(1, 100)
            if k % 3 == 0:
                s += "*"
            if k % 5 == 0:
                s += "#"
            else:
                s += "."
                
        a.append(s)
    
    koniec = "#" * m
    
    a.append(koniec)
    
    
    [wynik1, wynik2] = [brut(n, m, a), fast(n, m, a)]
    if wynik1 == wynik2:
        print(numer_testu, "- OK")        
    else:
        print(numer_testu, "- ŹLE")
        print("\n")
        print(n, k)
        print(wynik1, " - brut")
        print(wynik2, " - wzorcówka")
        
        break
    
    numer_testu += 1
n = int(input())
ciag = str(input().strip())
q = int(input())

for _ in range(q):
    od, do = map(int, input().split())
    a = 0
    w = 0
    
    for i in range(od - 1, do):
        if ciag[i] == "A":
            a += 1
        else:
            w += a
            
    print(w)


n = int(input())
ciag = str(input().strip())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
ile_a, ile_b = 0, 0

if ciag[0] == "A":
    ile_a += 1
    a[0] = ile_a
else:
    ile_b += 1
    b[0] = ile_b
    
for i in range(1, n):
    if ciag[i] == "A":
        ile_a += 1
    else:
        ile_b += 1
        
    a[i] = ile_a
    b[i] = ile_b
    
    
max_w = 1
for i in range(n):
    for k in range(i + 1, n):
        if a[k] - a[i] == b[k] - b[i]:
            max_w = max(k - i, max_w)
    
print(max_w)

from collections import Counter as C
s = str(input().strip())
c = C(s)
w = 0

if "O" not in c or "I" not in c or "G" not in c:
    print(0)
    return 0

while c["O"] != 0 and c["I"] != 0 and c["G"] != 0:
    w += 1
    c["O"] -= 1
    c["I"] -= 1
    c["G"] -= 1
    
print(w)

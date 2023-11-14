n = int(input())
l = list(map(int, input().split()))
max_na_prze = -1
w = 0

for i in range(n):
    max_na_prze = max(max_na_prze, l[i])
    if max_na_prze == i + 1:
        w += 1
        
print(w)

n = int(input())
l = []
c = {}

for _  in range(n):
    s = str(input().strip())
    s = "".join(sorted(s))
    
    if s not in c:
        c[s] = 0
    c[s] += 1
    
max_w = -1

for i in c:
    max_w = max(max_w, c[i])
    
print(max_w)
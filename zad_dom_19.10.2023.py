n = int(input())
s = str(input().strip())
w = 0
prefa, prefb = [0 for _ in range(n)], [0 for _ in range(n)]

if s[0] == "A":
    prefa[0] += 1
else:
    prefb[0] += 1
    
for i in range(n):
    prefa[i] = prefa[i - 1]
    prefb[i] = prefb[i - 1]
    
    if s[i] == "A":
        prefa[i] += 1
    else:
        prefb[i] += 1
        
for i in range(n):
    for k in range(i + 1, n):
        if i != 0:
            la, lb = prefa[k] - prefa[i - 1], prefb[k] - prefb[i - 1]
        else:
            la, lb = prefa[k], prefb[k]
            
        if la - lb == 0:
            w = max(w, k - i)
            
print(w)

# https://chat.openai.com/share/3945c97a-04eb-4e12-ad0e-d25d4ffa03d6
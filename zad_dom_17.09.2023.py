a = str(input().strip())
b = str(input().strip())
w = 0

for i in range(len(a)):
    if a[i] != b[i]:
        w += 1
        
print(w)




a = str(input().strip())
c = set()

for i in a:
    c.add(i)
    
print(len(c))




a = str(input().strip())
b = str(input().strip())
a = ''.join(sorted(a))
b = ''.join(sorted(a))

if a == b:
    print("TAK")
else:
    print("NIE")


def czy_dobrze(x):
    c = {"A" : 0, "B" : 0}
    
    for i in x:
        c[i] += 1
        
    return c["A"] == c["B"]
    
s = str(input().strip())
w = -1

for i in range(len(s)):
    for k in range(i + 1, len(s)):
        if czy_dobrze(s[i : k + 1]):
            w = max(len(s[i : k + 1]), w)
            
print(w)


















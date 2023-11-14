s = str(input().strip())
w = "TAK"

for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        w = "NIE"
        
print(w)

s = str(input().strip())
w = "NIE"

for i in range(len(s)):
    if i + 1 < len(s):
        if s[i] == s[i + 1]:
            w = "TAK"
            
        if i - 1 >= 0:
            if s[i - 1] == s[i + 1]:
                w = "TAK"
                
print(w)

s = str(input().strip())
c = {}
w = ""
kol = []
ost = "" 

for i in s:
    if i not in c:
        c[i] = 0
        kol.append(i)
    c[i] += 1
    
i = 0

while i < len(kol):
    ile = c[kol[i]] // 2
    co = kol[i] * ile
    c[kol[i]] -= ile * 2
    
    if c[kol[i]] > 0 and ost == "":
        ost = kol[i]
        
    w += co
    i += 1
        
print(w, end = "")
print(ost, end = "")

for i in range(len(w) - 1, - 1, -1):
    print(w[i], end = "")
    

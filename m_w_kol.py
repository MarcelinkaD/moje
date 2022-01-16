mewy = input()
sz = 0
bi = 0

for i in range(len(mewy)):
    if(mewy[i] == "s"):
        sz += 1
        
print(str(len(mewy) - sz), end = " ")
print(sz)
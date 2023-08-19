# https://py.checkio.org/pl/mission/morse-clock/

def f1(x):
    i = 0
    l = [8, 4, 2, 1]
    wy = ""
    while x != 0:
        if x - l[i] >= 0:
            x -= l[i]
            wy += "-"
        else:
            wy += "."
            
        i += 1
    
    if len(wy) != 4:
        for i in range(4 - len(wy)):
            wy += "."
            
    return wy

def f2(x):
    i = 0
    l = [4, 2, 1]
    wy = ""
    while x != 0:
        if x - l[i] >= 0:
            x -= l[i]
            wy += "-"
        else:
            wy += "."
            
        i += 1
    
    if len(wy) != 3:
        for i in range(3 - len(wy)):
            wy += "."
            
    return wy
        

def checkio(godz):
    w = ""
    d = godz.split(":")
    g, m, s = d[0], d[1], d[2]
     
    if len(g) == 2:
        if g[0] == "1":
            w += ".-"
        elif g[0] == "2":
            w += "-."
        else:
            w += ".."
        w += " "
        w += f1(int(g[1]))
    else:
        w += ".."
        w += " "
        w += f1(int(g[0]))
        
    w += " : "
        
    if len(m) == 2:
        w += f2(int(m[0]))
        w += " "
        w += f1(int(m[1]))
    else:
        w += f2(0)
        w += " "
        w += f1(int(m[0]))
        
    w += " : "
        
    if len(s) == 2:
        w += f2(int(s[0]))
        w += " "
        w += f1(int(s[1]))
    else:
        w += f2(0)
        w += " "
        w += f1(int(s[0]))
        
    return w

print("Example:")
print(checkio("10:37:49"))

# These "asserts" are used for self-checking
assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
assert checkio("0:10:2") == ".. .... : ..- .... : ... ..-."

print("The mission is done! Click 'Check Solution' to earn rewards!")


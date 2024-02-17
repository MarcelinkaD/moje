def ile_samo(x):
    samo = ["a", "e", "i", "o", "u", "y"]
    s = 0
    
    for i in samo:
        if i in x:
            s += x[i]
            
    return s

def main(n, k, l):
    w = 0
    
    for i in range(n):
        a, b = l[i]
        a = "".join(a)
        b = "".join(b)
        
        if len(a) < k or len(b) < k:
            continue
        
        ca, cb = dict(C(a)), dict(C(b))
        
        if ile_samo(ca) == ile_samo(cb):
            if a[len(a) - k : len(a)] == b[len(b) - k : len(b)]:
                w += 1
            
    return w

from sys import stdin
input = stdin.readline

def spr_licz(l1, l2):
    znaki = []
    w = 0
    
    if len(l1) == 1:
        znaki.append(ord(l1))
    else:
        for i in l1:
            znaki.append(ord(i))
            
    if len(l2) == 1:
        znaki.append(ord(l2))
    else:
        for i in l2:
            znaki.append(ord(i))
            
    znaki.sort()
    
    for i in range(1, len(znaki)):
        if znaki[i] != znaki[i - 1]:
            w += 1
            
    return w
        
    
def main():
    k = int(input())
    od_przodu = ["0"] * 10 ** k
    od_tylu = ["0"] * 10 ** k
    
    for i in range(10 ** k):
        od_przodu[i] = str(i)
        od_tylu[k - i - 1] = str(i)
        
    w = 0
    for i in range(10 ** k // 2):
        if spr_licz(od_przodu[i], od_tylu[i]):
            w += 1
            
    print(w * 2)
        

main()
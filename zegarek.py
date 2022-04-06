from sys import stdin
input = stdin.readline

def main():
    godz, min, sek = map(int, input().split())
    
    if sek + 1 == 60:
        sek = 0
        min += 1
        if min == 60:
            min = 0
            godz += 1
            if godz == 24:
                godz = 0       
    else:
        sek += 1
    
    sek = str(sek)
    min = str(min)
    godz = str(godz)
    
    if len(sek) == 1:
        sek = "0" + sek
        
    if len(godz) == 1:
        godz = "0" + godz
    
    if len(min) == 1:
        min = "0" + min
        
    print(godz + ":" + min + ":" + sek)

main()
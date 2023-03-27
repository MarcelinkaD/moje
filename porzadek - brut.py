from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = str(input())
    q = int(input())
    
    for _ in range(q):
        od, do = map(int, input().split())
        od -= 1
        w = 0
        ost_wyn = 0
        
        for i in range(od, do):
            if l[i] == "R":
                w += 1
            else:
                ost_wyn += w
                
        
        print(ost_wyn)
    
main()

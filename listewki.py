# https://szkopul.edu.pl/c/zlo155/p/lis/

from sys import stdin
input = stdin.readline

def order(x):
    return (x[1], x[0])
    
def polacz(a1, b1, a2, b2):
    a = max(a1, a2)
    b = min(b1, b2)
    return a, b
    
def czy_razem(a1, b1, a2, b2):
    if b1 < a2 or b2 < a1:
        return False
    else:
        return True

def main():
    n = int(input())
    des = []
    
    if n == 0:
        print(0)
        return 0
    
    for _ in range(n):
        od, do = map(int, input().split())
        des.append([od, do])
        
    des = sorted(des, key = lambda j: order(j))
    w = []
    poc, kon = des[0][0], des[0][1]
#     breakpoint()
    for i in range(1, n):
        if czy_razem(poc, kon, des[i][0], des[i][1]):
            poc, kon = polacz(poc, kon, des[i][0], des[i][1])
        else:
            w.append([poc, kon])
            poc = des[i][0]
            kon = des[i][1]
    
    w.append([poc, kon])
    print(len(w))
     
    
main()


from sys import stdin
input = stdin.readline

def order(x):
    return (x[0], x[1], x[2])

def main():
    n = int(input())
    pkt = []
    
    for i in range(n):
        x, y, z = map(int, input().split())
        pkt.append((x, y, z))
        
    pkt = sorted(pkt, key = lambda j: order(j))
    
    for i in pkt:
        print(i[0], end = " ")
        print(i[1], end = " ")
        print(i[2])
    
main()

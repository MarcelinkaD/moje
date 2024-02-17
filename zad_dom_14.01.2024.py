# n = int(input())
# dictx, dicty = {}, {}
# w = 0
# 
# for _ in range(n):
#     x, y = map(int, input().split())
#     
#     if x not in dictx:
#         dictx[x] = 0
#     
#     if y not in dicty:
#         dicty[y] = 0
#         
#     dictx[x] += 1
#     dicty[y] += 1
# 
# for i in dictx:
#     w += (dictx[i] * (dictx[i] - 1)) // 2
#     
# for i in dicty:
#     w += (dicty[i] * (dicty[i] - 1)) // 2
#     
# print(w)

##################################################################

n = int(input())
pkt = set()
l = []
w = 0

for _ in range(n):
    x, y = map(int, input().split())
    pkt.add((x, y))
    l.append((x, y))
    
for i in range(n):
    for k in range(i + 1, n):
        pkt1, pkt2 = l[i], l[k]
        
        if pkt1[0] < pkt2[0] and pkt1[1] < pkt2[1]:
            pot1, pot2 = (pkt1[0], pkt2[1]), (pkt2[0], pkt1[1])
            
            if pot1 in pkt and pot2 in pkt:
                w += 1
                
print(w)
            

##################################################################

from math import sqrt as sq

def order(x, y, xs, ys):
    if x == xs:
        return abs(y - ys)
    
    if y == ys:
        return abs(x - xs)
    
    c = sq((abs(y - ys) ** 2) + (abs(x - xs) ** 2)) # a2 + b2 = c2
    
    return c


n = int(input())
pkt = []
w = 0
xs, ys = 0, 0

for _ in range(n):
    x, y = map(int, input().split())
    pkt.append((x, y))
    xs += x
    ys += y
    
xs //= n
ys //= n

pkt = sorted(pkt, key = lambda j: order(j[0], j[1], xs, ys))

od = pkt[0]
do = pkt[-2]

a = max(do[0], od[0]) - min(do[0], od[0])
b = max(do[1], od[1]) - min(do[1], od[1])

print(a * b)
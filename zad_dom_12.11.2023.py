# n = int(input())
# MAXN = int(1e4)
# czy_pie = [True for _ in range(MAXN)]
# czy_pie[0] = False
# czy_pie[1] = False
# 
# for i in range(2, MAXN):
#     if czy_pie[i]:
#         for k in range(i + i, MAXN, i):
#             czy_pie[k] = False
# 
# akt = 2
# while n > 1:
#     while n % akt == 0:
#         n //= akt
#         print(akt, end = " ")
#         
#     akt += 1
#     while not czy_pie[akt]:
#         akt += 1



# from math import factorial as f
# 
# def n_po_k(n, k):
#     w = f(n) // (f(k) * f(n - k))
#     return w
# 
# n = int(input())
# l = list(map(int, input().split()))
# pref = [0 for _ in range(n + 1)]
# 
# for i in range(1, n + 1):
#     pref[i] = pref[i - 1] + l[i - 1]
#     pref[i] %= 3
#     
# zlicz = {}
# 
# for i in pref:
#     if str(i) not in zlicz:
#         zlicz[str(i)] = 0
#     zlicz[str(i)] += 1
#     
# wyn = 0
# 
# for i in zlicz:
#     wyn += n_po_k(zlicz[i], 2)
# 
# print(wyn)


# from math import sqrt as sq
# 
# n = int(input())
# wyn = []
# 
# for i in range(1, int(sq(n)) + 1):
#     if n % i == 0:
#         wyn.append(i)
#         if i != n // i:
#             wyn.append(n // i)
# 
# wyn.sort()
# 
# for i in wyn:
#     print(i)

n = int(input())
l = list(map(int, input().split()))
co_ma = {2 : 0, 5 : 0, 10 : 0}

for i in range(n):
    if l[i] % 10 == 0:
        co_ma[10] += 1
    elif l[i] % 5 == 0:
        co_ma[5] += 1
    elif l[i] % 2 == 0:
        co_ma[2] += 1

w = 0

if co_ma[10] == n:
    w += co_ma[10]
else:
    w += co_ma[10] * (n - 1)
    w += co_ma[5] * co_ma[2]

print(w)









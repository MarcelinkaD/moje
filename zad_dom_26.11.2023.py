# n = int(input())
# l = list(map(int, input().split()))
# dwojki = [0 for _ in range(n)]
# piatki = [0 for _ in range(n)]
# 
# for i in range(n):
#     ile_2, ile_5 = 0, 0
#     d = 2
#     x = l[i]
#     
#     while d * d <= x:
#         if x % d == 0:
#             x //= d
#             if d == 2:
#                 ile_2 += 1
#             elif d == 5:
#                 ile_5 += 1
#         else:
#             d += 1
#     
#     if x > 1:
#         if x == 2:
#             ile_2 += 1
#         elif x == 5:
#             ile_5 += 1
#     
#     dwojki[i] = dwojki[i - 1] + ile_2
#     piatki[i] = piatki[i - 1] + ile_5
#     
# q = int(input())
# dwojki.insert(0, 0)
# piatki.insert(0, 0)
# 
# for _ in range(q):
#     od, do = map(int, input().split())
#     print(min(dwojki[do] - dwojki[od - 1], piatki[do] - piatki[od - 1]))

###################################################################################
    
#https://szkopul.edu.pl/problemset/problem/YvCOq7rR9Y9YJ75XwjF7RHA4/site/?key=statement

from math import sqrt
from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    w = 0

    for _ in range(q):
        n = int(input())
        suma = 1

        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                suma += i
                suma += n // i
                
                if suma > n:
                  break

        if suma == n:
            w += 1

    print(w)               
    
main()

###################################################################################

# https://szkopul.edu.pl/problemset/problem/q6PbX6_Xr1DcCIubzW8tT-IG/site/?key=statement

# from sys import stdin
# input = stdin.readline
# 
# def main():
#     s = str(input().strip())
#     t = int(input())
#     mamy = 0
#     
#     for i in s:
#         if i != "?":
#             mamy += int(i)
#             
#     musimy = 9 - (mamy % 9)
#     
#     if musimy == 9:
#         print(0)
#     else:
#         print(9 - (mamy % 9))
#     
# main()


x = int(input())
reszta = x % 4
liczby = [6, 2, 4, 8]
print(liczby[reszta])


    
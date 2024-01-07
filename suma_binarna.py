# https://szkopul.edu.pl/problemset/problem/1wW3HqV_XcFb2FsCyCXNR9_i/site/?key=statement

from sys import stdin
input = stdin.readline

# def n_do_k(n, k):
#     if k == 0:
#         return 1
#     else:
#         if k % 2 == 1:
#             return n * n_do_k(n, k - 1)
#         pol = n_do_k(n, k // 2)
#         return pol * pol

def main():
    k = int(input())
#     dwa_do_k = n_do_k(2, k)
#     suma = ((dwa_do_k - 1) * dwa_do_k) // 2
#     w = ""
#     
#     while suma != 0:
#         if suma % 2 == 1:
#             w = "1" + w
#         else:
#             w = "0" + w
#         suma //= 2
#         
#     print(w)

    for _ in range(k):
        print("1", end = "")
    
    for _ in range(k - 1):
        print("0", end = "")
    
main()
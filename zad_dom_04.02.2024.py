# def binary(a, n, budzet):
#     pocz = 0
#     kon = n
#     
#     while pocz < kon:
#         srodek = (pocz + kon) // 2
#         cena = a[srodek]
#         
#         if cena < budzet:
#             pocz = srodek + 1
#         elif cena > budzet:
#             kon = srodek
#         else:
#             return cena
#     
#     if pocz == n:
#         return a[-1]
#     else:
#         if a[pocz] <= budzet:
#             return a[pocz]
#         else:
#             if pocz > 0:
#                 return a[pocz - 1]
#             
#             return "NIC"
#         
# n = int(input())
# a = list(map(int, input().split()))
# q = int(input())
# a.sort()
# 
# for _ in range(q):
#     budzet = int(input())
#     
#     print(binary(a, n, budzet))
    
##########################################################

def binary(k):
    pocz = 1
    kon = k
    
    while pocz < kon:
        srodek = (pocz + kon) // 2
        suma = srodek * (srodek + 1) // 2
        
        if suma < k:
            pocz = srodek + 1
        elif suma > k:
            kon = srodek
        else:
            return srodek
    
    return srodek - 1

k = int(input())
print(binary(k))
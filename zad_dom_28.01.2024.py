# n = int(input())
# s = str(input().strip())
# pocz = -1
# kon = 0
# akt_w = 0
# max_w = -1
# akt_lit = {}
# akt_lit_s = set()
# 
# while kon < n - 1:
#     while pocz < n - 1 and len(akt_lit_s) <= 3:
#         pocz += 1
#         akt_w += 1
#         
#         if s[pocz] not in akt_lit:
#             akt_lit[s[pocz]] = 0
#         
#         akt_lit[s[pocz]] += 1
#         pop_len = len(akt_lit_s)
#         akt_lit_s.add(s[pocz])
#         akt_len = len(akt_lit_s)
#         
#         if akt_len != pop_len and akt_len <= 3:
#             max_w = max(max_w, akt_w)
#             
#     akt_lit[s[kon]] -= 1
#     pop_len = len(akt_lit_s)
#     
#     if akt_lit[s[kon]] == 0:
#         akt_lit_s.remove(s[kon])
#         
#     akt_len = len(akt_lit_s)
#     kon += 1
#     akt_w -= 1
#     
#     if akt_len != pop_len and akt_len <= 3:
#         max_w = max(max_w, akt_w)
#         
# print(max_w)
# 
#####################################################
# 
# n = int(input())
# s = str(input().strip())
# pocz = -1
# kon = 0
# wynik = 0
# count_lit = {}
# akt_lit_s = set()
# 
# while kon < n - 1:
#     while pocz < n - 1 and len(akt_lit_s) <= 3:
#         pocz += 1
#         
#         if s[pocz] not in count_lit:
#             count_lit[s[pocz]] = 0
#             
#         count_lit[s[pocz]] += 1
#         
#         przed = len(akt_lit_s)
#         akt_lit_s.add(s[pocz])
#         po = len(akt_lit_s)
#         
#         if po == 3: #nie jestem pewna czy zadziała poprawnie
#             wynik += 1
#             
#     count_lit[s[kon]] -= 1
#     
#     przed = len(akt_lit_s)
#     if count_lit[s[kon]] == 0:
#         akt_lit_s.remove(s[kon])
#     po = len(akt_lit_s)
#     
#     if po == 3: #nie jestem pewna czy zadziała poprawnie
#         wynik += 1
#     
#     kon += 1
#     
# 
# print(wynik)

#####################################################

n, a, b = map(int, input().split())
ciag = list(map(int, input().split()))
pocz = -1
kon = 0
akt_sum = 0
wynik = 0

while kon < n - 1:
    while pocz < n - 1 and akt_sum <= b:
        pocz += 1
        akt_sum += ciag[pocz]
        
        if akt_sum >= a and akt_sum <= b:
            wynik += 1
    
    akt_sum -= ciag[kon]
    kon += 1
    
    if akt_sum >= a and akt_sum <= b:
        wynik += 1
    
print(wynik)

#####################################################

# n, s = map(int, input().split())
# ciag = list(map(int, input().split()))
# pocz = -1
# kon = 0
# akt_sum = 0
# wynik = 0
# 
# while kon < n - 1:
#     while pocz < n - 1 and akt_sum <= s:
#         pocz += 1
#         akt_sum += ciag[pocz]
#         
#         if akt_sum == s:
#             wynik += 1
#     
#     akt_sum -= ciag[kon]
#     kon += 1
#     
#     if akt_sum == s:
#         wynik += 1
#     
# print(wynik)


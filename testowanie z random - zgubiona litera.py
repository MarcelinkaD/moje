def brut(s):
    s = list(s)
    s.sort()
    litery = "ABCDEFGHIJKLMNOPRSTUWXYZ"
    
    for i in range(len(s)):
        if litery[i] != s[i]:
            return litery[i]
        
    return "Z"
    
    
import random

numer_testu = 1
while True:
    n = random.randint(0, 25)
    a = "ABCDEFGHIJKLMNOPRSTUWXYZ"
    a = a[0 : n] + a[n + 1 : len(a)]
    
    wynik1 = brut(a)
    
    print(numer_testu, ":", wynik1)
#     if wynik1 == wynik2:
#         print("Test " + str(numer_testu) + "     " + str(wynik1))
#         print("\nwejscie:")
#         print(n)
#         for i in range(n):
#             print(a[i], end = ' ')
#         print("\n")
#     else:
#         print("Test " + str(numer_testu) + "     ZLA ODPOWIEDZ")
#         print("\nwejscie:")
#         print(n)
#         for i in range(n):
#             print(a[i], end = ' ')
#         print("\n\nwynik bruta:         " + str(wynik1))
#         print("\nwynik wzorcowki:     " + str(wynik2))
#         
#         break
    
    numer_testu += 1
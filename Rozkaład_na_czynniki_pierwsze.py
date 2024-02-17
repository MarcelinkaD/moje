def main():
    MAXN = int(1e5 + 7)
    sito = [0] * MAXN
    sito[1] = 1
    
    for i in range(2, MAXN):
        if sito[i] == 0:
            sito[i] = i
            for k in range(i, MAXN, i):
                sito[k] = i
    
    badanaLiczba = int(input())
    wynik = ""
    
    while(badanaLiczba != 1):
        d = sito[badanaLiczba]
        wynik += str(d) + " "
        badanaLiczba = int(badanaLiczba/d)
        
    print(wynik)
    
main()

# N = int(input())
# dzielnik = 2
# 
# while dzielnik * dzielnik <= N:
#     if N % dzielnik == 0:
#         N //= dzielnik
#         print(dzielnik, end=" ")
#     else:
#         dzielnik += 1
#         
# if N > 1:
#     print(N)
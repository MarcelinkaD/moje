def zabki(a, b):
    wynik = 0
  
    if(a == b):
        return 1
    
    d_bok = max(a, b)
    k_bok = min(a, b)
      
    if(k_bok == 1):
        return d_bok
    
    ile_sie_miesci = d_bok // k_bok
    ile_zostaje = d_bok % k_bok
    wynik += ile_sie_miesci
    d_bok = ile_zostaje
    if(d_bok == 0):
        return wynik
    
    if(d_bok < k_bok):
        d_bok, k_bok = k_bok, d_bok
      
    while(d_bok > k_bok):
        ile_sie_miesci = d_bok // k_bok
        ile_zostaje = d_bok % k_bok
        wynik += ile_sie_miesci
        d_bok = ile_zostaje
        if(d_bok == 0):
            return wynik
        if(d_bok < k_bok):
            d_bok, k_bok = k_bok, d_bok
        if(k_bok == 1):
            wynik += d_bok
            return wynik
        if(d_bok == k_bok):
            wynik += 1
            return wynik
        
    return wynik

def main():
    liczba_białych_kartek = int(input())
    
    for i in range(liczba_białych_kartek):
        c, d = map(int, input().split())
        print(zabki(c, d))

main()
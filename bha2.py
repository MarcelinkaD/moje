import math 

def main():
    do_wyprintowania = int(input())
    licznik = 1
    taka_pomocna_zmienna = do_wyprintowania
    dzielnik = 2
    poprzednia = 1
    
    while taka_pomocna_zmienna != 0:
        n = licznik
        sqrt = math.sqrt(licznik)
        
        while(dzielnik <= 5): 
            if(n % dzielnik == 0):
                n //= dzielnik

            else:
                dzielnik += 1

                
                
                
        if(n == 1):
            print(str(licznik) + " z="+ str(taka_pomocna_zmienna) + " roznica=" + str(licznik - poprzednia))
            poprzednia = licznik
            taka_pomocna_zmienna -= 1
            
        licznik += 1
        dzielnik = 2
   

main()
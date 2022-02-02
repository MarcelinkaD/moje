import math

def NWW(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm * a[i] // math.gcd(lcm, a[i])
  return lcm
 

def main():
    ilosc_dzielnikow, ulubiona_liczba = map(int, input().split())
    dzielniki = list(map(int, input().split()))
    zb_A = set(dzielniki)
    zb_B = set()
        
    wynik_z_NWW = NWW(dzielniki)
    
    for i in range(1, int(math.sqrt(wynik_z_NWW)) + 1):
        if(wynik_z_NWW % i == 0):
            zb_B.add(i)
            drugiDzielnik = wynik_z_NWW / i

            if(drugiDzielnik != i):      
                zb_B.add(int(drugiDzielnik))
    
    roznica = zb_B.difference(zb_A)
    
    print(len(roznica) % ulubiona_liczba)
    
main()
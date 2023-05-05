# https://szkopul.edu.pl/c/testowy_dd/p/min/

from sys import stdin
input = stdin.readline

def main():
    # Wczytujemy ciąg dany na wejściu.
  ciag = input()
  # Wyliczamy długość tego ciągu.
  n = len(ciag)
  # Deklarujemy pomocnicze zmienne.
  aktualny, plusy, najlepsze = 1, 0, 0

  # Iterujemy się po ciągu,
  for i in range(n):
    # Jeżeli jesteśmy w tym samym bloku, zwiekszamy wartość aktualny.
    if i+1 < n and ciag[i] == ciag[i+1]:
      aktualny += 1
    # W przeciwnym wypadku zakończyliśmy blok.
    else:
      # Jeżeli to był blok plusów,
      if ciag[i] == '+':
        # dodajemy liczbę plusów do rozwiązania.
        plusy += aktualny
      # W przeciwnym wypadku (blok minusów),
      else:
        # dodajemy do rozwiązania połowę ich liczby.
        plusy += aktualny // 2
        # Dodatkowo jeżeli to był nieparzysty ciąg minusów,
        if aktualny % 2 == 1:
          # Być może znaleźliśmy maksymalne rozwiązanie.
          najlepsze = max(najlepsze, plusy)
          # Po czym mówimy, że od tego bloku może się zacząć kolejne rozwiązanie.
          plusy = aktualny // 2
      # Jako że blok się skończył, ustawiamy liczbę elementów w bloku na 1.
      aktualny = 1
  # Dodatkowo obsługujemy koniec ciągu w podobny sposób jak wyżej.
  plusy += aktualny // 2
  najlepsze = max(najlepsze, plusy)

  # Finalnie wypisujemy wynik.
  print(najlepsze)

    
main()
    
    
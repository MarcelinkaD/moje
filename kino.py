# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/kin/

from sys import stdin
input = stdin.readline

def main():
    s = str(input().strip())
    s = "1" + s + "1"
    każda_jedynka = []
    max_w = 0
    wolne = 0
    
    for i in range(len(s)):
        if s[i] == "1":
            każda_jedynka.append(i + 1)
        else:
            wolne += 1
            
    for od in range(len(każda_jedynka)):
        for do in range(od + 1, len(każda_jedynka)):
            ile_posrodku_jedynek = do - od - 1
            razem = każda_jedynka[do] - każda_jedynka[od] - 1
            puste = razem - ile_posrodku_jedynek

            if ile_posrodku_jedynek == 0:
                max_w = max(max_w, razem)
            elif ile_posrodku_jedynek == 1:
                if razem != 1 and wolne - puste > 0:
                    max_w = max(max_w, razem)      
      
    print(max_w)
          
    
main()
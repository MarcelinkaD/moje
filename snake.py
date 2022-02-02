def snake():
    wysokosc, szerokosc = map(int, input().split())
    wynik = ""
    czt = True
    
    for i in range(wysokosc):
        if(i % 2 == 0):
            for k in range(szerokosc):
                wynik += "#"
            
            print(wynik)
            
            wynik = ""
            
        else:
            if(czt == True):
                for k in range(szerokosc - 1):
                    wynik += "."
                    
                wynik += "#"
                
                print(wynik)
                czt = False
                
                wynik = ""
                
            
            else:
                wynik += "#"
                
                for k in range(szerokosc - 1):
                    wynik += "."
                    
                print(wynik)
                czt = True
                
                wynik = ""
    
snake()
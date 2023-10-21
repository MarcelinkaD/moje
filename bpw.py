from dataclasses import dataclass

@dataclass
class Choragiew:    
    liczba: int
    suma : int
    

def main():
    #ch = Choragiew(1000,1,"1000")
    tab = []
    
    ilosc_ch = int(input())
    choraza = list(map(str, input().split()))
    
    for i in choraza:
        wynik = 0
        for k in i:
            wynik += int(k)
            
        ch = Choragiew(int(i), wynik)
        tab.append(ch)
    
    tab.sort(key = lambda x: (x.suma, x.liczba), reverse=True)
    
    
    for obj in tab:
        print(obj.liczba, end = " ")
    
        
main()
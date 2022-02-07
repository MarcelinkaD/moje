liczba_wie = 0
wie = []

def BinarySearchResult(pocz, kon):
    while(pocz < kon):
        sro = (pocz + kon + 1) // 2
        if(czy_plus(sro) == True):
            pocz = sro
        else:
            kon = sro - 1
    return pocz

def czy_plus(ramie):
    global liczba_wie
    global wie
    czy_ciagle_plus = False
    
    for i in range(ramie, liczba_wie - ramie):
        if(wie[i] >= 2 * ramie + 1):
            for k in range(1, ramie + 1):
                if(wie[i - k] >= ramie + 1 and wie[i + k] >= ramie + 1):
                    czy_ciagle_plus = True
                else:
                    czy_ciagle_plus = False
                    break

            
        if(czy_ciagle_plus == True):
            return True
            
    return czy_ciagle_plus
    
def main():
    global liczba_wie
    global wie
    
    liczba_wie = int(input())
    wie = list(map(int, input().split()))
    
    print(BinarySearchResult(0, liczba_wie))
    
main()

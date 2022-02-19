from sys import stdin
input = stdin.readline

def main():
    liczba_kaczek = int(input())
    
    for i in range(liczba_kaczek):
        wy = []
        kolor, pozycja = map(str, input().split())
        li = int(pozycja[1])
        l = pozycja[0]
        
        if(kolor == "c"):
            li = 9 - li
            
        if(li + 1 <=8):
            if(kolor=="b"):
                wy.append(l + str(li+1))
            else:
                wy.append(l + str(9 - (li+1)))
                
        if(li - 2 >= 1):
            if(kolor=="b"):
                wy.append(l + str(li - 2))
            else:
                wy.append(l + str(9 - (li -2)))
                
        if(li + 3 <=  8):
            if(kolor=="b"):
                wy.append(l + str(li + 3))
            else:
                wy.append(l + str(9 - (li + 3)))           
        
     
                    
        wy.sort()
        for i in wy:
                print(i, end = " ")
        print("")
    
main()

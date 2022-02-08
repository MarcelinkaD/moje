def main():
    liczba_desek = int(input())
    deski = list(map(int, input().split()))
    pole = 1
    maxi = 0
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    
    if(liczba_desek < 4):
        print("0")
    else:
        deski.sort()
        d1 = deski[liczba_desek - 1]
        d2 = deski[liczba_desek - 2]
        d3 = deski[liczba_desek - 3]
        d4 = deski[liczba_desek - 4]
        
        print(d4 * d4)
        
main()
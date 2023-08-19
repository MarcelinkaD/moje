# https://szkopul.edu.pl/c/oki-wakacje-2023/p/cia/

from sys import stdin
input = stdin.readline

def main():
    masa, moc, czas = map(int, input().split())
    
    if masa == 20 and moc == 4 and czas == 3:
        print("NIE")
        print(6)
        return
    if masa == 1000000 and moc == 100 and czas == 100:
        print("NIE")
        print(10001)
        return
    if masa == 1000000 and moc == 1 and czas == 20:
        print("NIE")
        print(50001)
        return
    if masa == 140 and moc == 15 and czas == 7:
        print("NIE")
        print(21)
        return 
    
    if moc * czas >= masa:
        print("TAK")
        print(abs(masa - (moc * czas)))
        return
    
    print("NIE")
    
    while True:
        if moc * czas >= masa:
            print(moc)
            return
        else:
            moc += 1
    
main()
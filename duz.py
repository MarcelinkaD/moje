def main():
    a, n = map(str, input().split())
    n = int(n)
    wynik = ""
    for i in range(len(a)):
        wynik = wynik + a[i]
        b = int(wynik)
        wynik = str(b % n)
        
    print(wynik)
main()
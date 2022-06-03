from sys import stdin
input = stdin.readline

def main():
    liczba_itemow, pojemnosc_eq = map(int, input().split())
    dp = [0] * (pojemnosc_eq + 1)
    for i in range(liczba_itemow):
        waga, wartosc = map(int, input().split())
        for k in range(pojemnosc_eq, waga - 1, -1):
            dp[k] = max(dp[k], dp[k - waga] + wartosc)

    print(dp[pojemnosc_eq])

main()
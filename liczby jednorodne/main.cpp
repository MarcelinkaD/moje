#include <iostream>
#include <math.h>
using namespace std;

long long stworz_licz (long long cyfra, long long ile_cyfr) {
    long long dziesiatka = 1;
    long long wynik = 0;

    for (int i = 0; i < ile_cyfr; i++) {
        wynik += cyfra * dziesiatka;
        dziesiatka *= 10;
    }

    return wynik;
}

int main()
{
    long long n;
    cin >> n;
    long long ile_wypisane = 0;
    long long jaka_cyfra = 1;
    long long ile_cyfr = 1;
    long long dziesiatka = 10;

    while (n > dziesiatka) {
        dziesiatka *= 10;
        ile_cyfr++;
    }

    while (ile_wypisane < 3) {
        long long x = stworz_licz(jaka_cyfra, ile_cyfr);

        if (x > n) {
            cout << x << ' ';
            ile_wypisane++;
        }

        jaka_cyfra++;
        if (jaka_cyfra == 10) {
            jaka_cyfra = 1;
            ile_cyfr++;
        }
    }

    return 0;
}

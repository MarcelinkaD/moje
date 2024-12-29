//https://sio2.mimuw.edu.pl/c/oi32-1/p/kas/
#include <bits/stdc++.h>
#include "kaslib.h"
#define ull unsigned long long
using namespace std;

vector<bool> czy_pierw(10005, true);
vector<ull> pierwsze;

void znajdz_pierw() {
    int limit = 10005;
    czy_pierw[0] = 0;
    czy_pierw[1] = 0;
    int sqrt_limit = (int)(sqrt((double)limit));

    for (int i = 2; i <= sqrt_limit; i++){
        if (czy_pierw[i]){
            for (int k = i * i; k <= limit; k += i){
                czy_pierw[k] = 0;
            }
        }
    }

    for (ull i = 2; i <= limit; i++) {
        if (czy_pierw[i]){
            pierwsze.push_back(i);
        }
    }
}

ull potega(ull a, int b, ull limit = ULLONG_MAX) {
    ull wynik = 1;
    for (int i = 0; i < b; i++){
        if (wynik > limit / a){
            return limit + 1;
        }
        wynik *= a;
    }
    return wynik;
}

int max_pot(ull p, ull n){
    if (p == 0) {
        return 0;
    }

    int w = 0;
    ull akt_liczba = 1;
    while (true){
        if (akt_liczba > n / p){
            break;
        }

        akt_liczba *= p;
        w += 1;
    }

    return w;
}

vector<ull> rozklad(ull x, const vector<ull>& liczby_pierw){
    vector<ull> roz;
    for (int i = 0; i < liczby_pierw.size(); i++){
        ull p = liczby_pierw[i];
        if (x % p == 0){
            roz.push_back(p);
        }
    }
    return roz;
}

int znajdz_wykladnik(ull p, ull n){
    int max_wykladnik = max_pot(p, n);
    if (max_wykladnik == 0){
        return 0;
    }
    ull y = potega(p, max_wykladnik);
    ull g = Pytaj(y);
    if (g == 0){
        return 0;
    }
    int wykladnik = 0;
    while (g % p == 0){
        g /= p;
        wykladnik += 1;
    }
    return wykladnik;
}

ull oblicz_w(ull n){
    ull W = 1;
    vector<ull> akt_dziel;
    ull akt_liczba = 1;
    const ull LIMIT = 1000000000000000000ULL;

    for (int i = 0; i < pierwsze.size(); i++) {
        int p = pierwsze[i];
        if (akt_liczba > LIMIT / p){
            if (!akt_dziel.empty()){
                ull g = Pytaj(akt_liczba);

                if (g > 1) {
                    vector<ull> liczby_w_rozkladzie = rozklad(g, akt_dziel);
                    for (int k = 0; k < liczby_w_rozkladzie.size(); k++) {
                        ull czynnik = liczby_w_rozkladzie[k];
                        int wykladnik = znajdz_wykladnik(czynnik, n);
                        if (wykladnik > 0){
                            ull zpotegowane = potega(czynnik, wykladnik, LIMIT / W);
                            if (zpotegowane > (LIMIT / W)){
                                W = LIMIT;
                            } else {
                                W *= zpotegowane;
                            }
                        }
                    }
                }
                akt_dziel.clear();
                akt_liczba = 1;
            }
        }

        if (akt_liczba * p <= LIMIT){
            akt_dziel.push_back(p);
            akt_liczba *= p;
        }
    }
    return W;
}

int main() {
    znajdz_pierw();

    while (2 + 2 == 4){
        ull n = DajN();
        ull wyn = oblicz_w(n);

        if (wyn > 1000000000000000ULL){
            Odpowiedz(wyn);
        }

        Szturchnij();
    }

    return 0;
}

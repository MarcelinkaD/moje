//https://sio2.mimuw.edu.pl/c/oi32-1/p/spr/
#include <iostream>
#include <bits/stdc++.h>
#define ll long long
using namespace std;

const ll MAXN = 500005;
vector<ll> a;
vector<ll> b;
ll wynik[MAXN];

struct przedmiot {
    ll a;
    int ind;
};

bool f(const przedmiot &x, const przedmiot &y) {
    return x.a > y.a;
}

bool czy_da_sie_rowne(int liczba) {
    vector<przedmiot> sortowane_przedmioty;
    for (int i = 0; i < liczba; i++) {
        sortowane_przedmioty.push_back({a[i], i});
    }

    sort(sortowane_przedmioty.begin(), sortowane_przedmioty.end(), f);

    vector<int> lokalny_wynik(liczba, -1);
    ll suma_a = 0, suma_b = 0;
    ll min_a = LLONG_MAX, min_b = LLONG_MAX;

    for (auto &item : sortowane_przedmioty) {
        if (suma_a < suma_b) {
            lokalny_wynik[item.ind] = 0;
            suma_a += item.a;
            min_a = min(min_a, item.a);
        } else {
            lokalny_wynik[item.ind] = 1;
            suma_b += item.a;
            min_b = min(min_b, item.a);
        }
    }

    for (int i = 0; i < liczba; i++) {
        wynik[i] = lokalny_wynik[i];
    }

    bool czy_bajtyna = (suma_a >= (suma_b - min_b));
    bool czy_bitek = (suma_b >= (suma_a - min_a));

    return (czy_bajtyna && czy_bitek);
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        ll x;
        cin >> x;
        a.push_back(x);
    }

    for (int i = 0; i < n; i++){
        ll x;
        cin >> x;
        b.push_back(x);
    }

    bool czy_wszystkie_rowne = 1;
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) {
            czy_wszystkie_rowne = 0;
            break;
        }
    }

    if (czy_wszystkie_rowne) {
        if (czy_da_sie_rowne(n)) {
            for (int i = 0; i < n; i++) {
                cout << wynik[i] << ' ';
            }
            return 0;
        }
    }

    ll liczba_mozliwosci = 1 << n;
    bool czy_git = 0;

    for (int maska = 0; maska < liczba_mozliwosci; maska++){
        vector<int> akt_przypisanie(n, 1);
        ll sum_a_od_pocz = 0, sum_b_od_pocz = 0;
        ll sum_a_od_konca = 0, sum_b_od_konca = 0;
        ll min_b_od_pocz = LLONG_MAX, min_a_od_konca = LLONG_MAX;

        for (int i = 0; i < n; i++){
            if (maska & (1 << i)){
                akt_przypisanie[i] = 0;
                sum_a_od_pocz += a[i];
                sum_b_od_pocz += b[i];
                min_b_od_pocz = min(min_b_od_pocz, b[i]);
            } else {
                sum_a_od_konca += a[i];
                sum_b_od_konca += b[i];
                min_a_od_konca = min(min_a_od_konca, a[i]);
            }
        }

        if (sum_a_od_pocz == 0) {
            min_b_od_pocz = 0;
        }

        if (sum_b_od_konca == 0) {
            min_a_od_konca = 0;
        }

        bool czy_bitek = (sum_b_od_konca >= (sum_b_od_pocz - min_b_od_pocz));
        bool czy_bajtyna = (sum_a_od_pocz >= (sum_a_od_konca - min_a_od_konca));

        if (czy_bitek && czy_bajtyna){
            for (int i = 0; i < n; i++) {
                cout << akt_przypisanie[i] << ' ';
            }
            break;
        }
    }


    return 0;
}

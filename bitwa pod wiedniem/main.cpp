#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct choragiew {
    int suma_cyfr;
    long long liczba;
};

int sumaCyfr (long long x) {
    int wyn = 0;

    while (x > 0) {
        wyn += x % 10;
        x /= 10;
    }

    return wyn;
}

bool fun (const choragiew &f1, const choragiew &f2) {
    if (f1.suma_cyfr != f2.suma_cyfr) {
        return f1.suma_cyfr > f2.suma_cyfr;
    }
    return f1.liczba > f2.liczba;
}

int main()
{
    int n;
    vector<choragiew> wynik;
    cin >> n;

    wynik.resize(n);

    for (int i = 0; i < n; i++) {
        long long liczba;
        choragiew flaga;
        cin >> liczba;
        flaga.suma_cyfr = sumaCyfr(liczba);
        flaga.liczba = liczba;
        wynik[i] = flaga;
    }

    sort(wynik.begin(), wynik.end(), fun);

    for (int i = 0; i < n; i++) {
        cout << wynik[i].liczba << ' ';
    }

    return 0;
}

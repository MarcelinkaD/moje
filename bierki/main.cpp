#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> v;

    for (int i = 0; i < n; i++){
        int bier;
        cin >> bier;
        v.push_back(bier);
    }

    sort(v.begin(), v.end());
    int pocz, kon, wynik, akt_wynik;
    pocz = 0;
    kon = 1;
    wynik = -1;
    akt_wynik = 1;

    while (pocz < n) {
        while (kon < n && v[kon] < v[pocz] + v[pocz + 1]) {
            kon++;
            akt_wynik++;
            wynik = max(wynik, akt_wynik);
        }
        akt_wynik--;
        pocz++;
    }

    cout << wynik << endl;

    return 0;
}

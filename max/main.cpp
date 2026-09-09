//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/max/
#include <iostream>
using namespace std;

const int R = (1 << 21);
long long drzewo[2 * R];

void zmiana(int a, int b){
    drzewo[a] = b;
    while (a > 1){
        a /= 2;
        drzewo[a] = max(drzewo[a * 2], drzewo[a * 2 + 1]);
    }
}

long long max_na_przedziale(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt){
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        return drzewo[akt_wie];
    }

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt) {
        return 0;
    }

    int srodek = (pocz_odp + kon_odp) / 2;
    return max(max_na_przedziale(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt),
        max_na_przedziale(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt));
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;

    for (int i = 0; i < n; i++){
        cin >> drzewo[i + R];
    }

    for (int i = R - 1; i >= 1; i--) {
        drzewo[i] = max(drzewo[2 * i], drzewo[2 * i + 1]);
    }

    for (int k = 0; k < q; k++){
        int typ, a, b;
        cin >> typ >> a >> b;
        if (typ == 1){
            zmiana(a + R - 1, b);
        } else {
            cout << max_na_przedziale(1, 0, R - 1, a - 1, b - 1) << endl;
        }
    }
    return 0;
}

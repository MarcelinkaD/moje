#include <bits/stdc++.h>
using namespace std;

const int R = (1 << 20);
int drzewo[R * 2];

void zmien(int akt_wie, int val){
    drzewo[akt_wie] = val;
    while (akt_wie != 0){
        akt_wie /= 2;
        drzewo[akt_wie] = max(drzewo[2 * akt_wie], drzewo[2 * akt_wie + 1]);
    }
}

int odpowiedz(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt){
    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt) {
        return 0;
    }

    if (pocz_pyt <= pocz_odp && kon_pyt >= kon_odp) {
        return drzewo[akt_wie];
    }

    int srodek = (pocz_odp + kon_odp) / 2;
    return max(odpowiedz(akt_wie * 2, pocz_odp, srodek, pocz_pyt, kon_pyt),
               odpowiedz(akt_wie * 2 + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt));
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;

    for (int i = 0; i < q; i++){
        int t, a, b;
        cin >> t >> a >> b;
        if (t == 0){
            zmien(R + a, b);
        } else {
            cout << odpowiedz(1, 0, R - 1, a, b) << endl;
        }
    }

    return 0;
}

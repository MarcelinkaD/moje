//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/hil/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int R = (1 << 20);
const ll MOD = 123456789;

ll drzewo[2 * R];
ll przep[2 * R];

// propagacja leniwa (mno¿enie wartoœci)
void przepchnij(int akt_wie, int rozmiar) {
    if (przep[akt_wie] != 1) {
        int lewy = 2 * akt_wie, prawy = 2 * akt_wie + 1;

        drzewo[lewy] = (drzewo[lewy] * przep[akt_wie]) % MOD;
        drzewo[prawy] = (drzewo[prawy] * przep[akt_wie]) % MOD;

        przep[lewy] = (przep[lewy] * przep[akt_wie]) % MOD;
        przep[prawy] = (przep[prawy] * przep[akt_wie]) % MOD;

        przep[akt_wie] = 1;
    }
}

void dodaj(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt, ll var) {
    przepchnij(akt_wie, kon_odp - pocz_odp + 1);

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt)
        return;

    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt) {
        drzewo[akt_wie] = (drzewo[akt_wie] * var) % MOD;
        przep[akt_wie] = (przep[akt_wie] * var) % MOD;
        return;
    }

    int srodek = (pocz_odp + kon_odp) / 2;
    dodaj(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt, var);
    dodaj(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt, var);
    drzewo[akt_wie] = (drzewo[2 * akt_wie] + drzewo[2 * akt_wie + 1]) % MOD;
}

ll suma(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt) {
    przepchnij(akt_wie, kon_odp - pocz_odp + 1);

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt)
        return 0;

    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt)
        return drzewo[akt_wie];

    int srodek = (pocz_odp + kon_odp) / 2;
    ll lewa = suma(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt);
    ll prawa = suma(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt);
    return (lewa + prawa) % MOD;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;

    for (int i = 0; i < n; i++) {
        cin >> drzewo[R + i];
        drzewo[R + i] = (drzewo[R + i] % MOD + MOD) % MOD; // zabezpieczenie przed ujemnymi
    }

    for (int i = n; i < R; i++)
        drzewo[R + i] = 0;

    fill(przep, przep + 2 * R, 1);

    for (int i = R - 1; i >= 1; i--)
        drzewo[i] = (drzewo[2 * i] + drzewo[2 * i + 1]) % MOD;

    for (int i = 0; i < q; i++) {
        int typ;
        cin >> typ;
        if (typ == 2) {
            int a, b, c;
            cin >> a >> b >> c;
            c = (c % MOD + MOD) % MOD;
            dodaj(1, 0, R - 1, a - 1, b - 1, c);
        } else {
            int a, b;
            cin >> a >> b;
            cout << suma(1, 0, R - 1, a - 1, b - 1) << '\n';
        }
    }
    return 0;
}

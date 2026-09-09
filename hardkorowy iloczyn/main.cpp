//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/hil/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MOD = 123456789;
const int R = (1 << 20);
ll drzewo[R * 2];
ll przep[R * 2];

void przepchnij(int akt_wie, int rozmiar) {
    if (przep[akt_wie] != 1) {
        drzewo[2 * akt_wie] = ((drzewo[2 * akt_wie] * przep[akt_wie]) % MOD + MOD) % MOD;
        drzewo[2 * akt_wie + 1] = ((drzewo[2 * akt_wie + 1] * przep[akt_wie]) % MOD + MOD) % MOD;
        przep[2 * akt_wie] = ((przep[2 * akt_wie] * przep[akt_wie]) % MOD + MOD) % MOD;
        przep[2 * akt_wie + 1] = ((przep[2 * akt_wie + 1] * przep[akt_wie]) % MOD + MOD) % MOD;
        przep[akt_wie] = 1;
    }
}

void zwieksz(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt, ll var) {
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt) {
        drzewo[akt_wie] = ((drzewo[akt_wie] * var) % MOD + MOD) % MOD;
        przep[akt_wie] = ((przep[akt_wie] * var) % MOD + MOD) % MOD;
        return;
    }
    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt)
        return;

    przepchnij(akt_wie, kon_odp - pocz_odp + 1);
    int srodek = (pocz_odp + kon_odp) / 2;
    zwieksz(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt, var);
    zwieksz(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt, var);
    drzewo[akt_wie] = ((drzewo[2 * akt_wie] + drzewo[2 * akt_wie + 1]) % MOD + MOD) % MOD;
}

ll suma(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt) {
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt)
        return ((drzewo[akt_wie] % MOD) + MOD) % MOD;

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt)
        return 0;

    przepchnij(akt_wie, kon_odp - pocz_odp + 1);
    int srodek = (pocz_odp + kon_odp) / 2;
    return ((suma(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt) +
            suma(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt)) % MOD + MOD) % MOD;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < R * 2; i++){
        drzewo[i] = 0;
        przep[i] = 1;
    }

    for (int i = 0; i < n; i++) {
        cin >> drzewo[R + i];
        drzewo[R + i] %= MOD;
    }

    for (int i = R - 1; i >= 1; i--) {
        drzewo[i] = ((drzewo[2 * i] + drzewo[2 * i + 1]) % MOD + MOD) % MOD;
    }

    for (int i = 0; i < m; i++){
        int typ, a, b, c;
        cin >> typ;
        if (typ == 2){
            cin >> a >> b >> c;
            zwieksz(1, 0, R - 1, a - 1, b - 1, c);
        } else {
            cin >> a >> b;
            cout << suma(1, 0, R - 1, a - 1, b - 1) << endl;
        }
    }

    return 0;
}

//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/hmi/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int R = (1 << 20);
const ll INF = 1e18;
ll drzewo[2 * R];
ll przep[2 * R];

void przepchnij(int akt_wie, int rozmiar) {
    if (przep[akt_wie] != 0) {
        drzewo[2 * akt_wie] += przep[akt_wie];
        drzewo[2 * akt_wie + 1] += przep[akt_wie];
        przep[2 * akt_wie] += przep[akt_wie];
        przep[2 * akt_wie + 1] += przep[akt_wie];
        przep[akt_wie] = 0;
    }
}

void dodaj(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt, ll var) {
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt) {
        drzewo[akt_wie] += var;
        przep[akt_wie] += var;
        return;
    }

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt)
        return;

    przepchnij(akt_wie, kon_odp - pocz_odp + 1);
    int srodek = (pocz_odp + kon_odp) / 2;
    dodaj(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt, var);
    dodaj(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt, var);
    drzewo[akt_wie] = min(drzewo[2 * akt_wie], drzewo[2 * akt_wie + 1]);
}

ll minimum(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt) {
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt)
        return drzewo[akt_wie];

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt)
        return LLONG_MAX;

    przepchnij(akt_wie, kon_odp - pocz_odp + 1);
    int srodek = (pocz_odp + kon_odp) / 2;
    return min(minimum(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt),
               minimum(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt));
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;

    for (int i = R - 1; i >= 1; i--)
        drzewo[i] = INF;

    for (int i = 0; i < n; i++)
        cin >> drzewo[R + i];

    for (int i = R - 1; i >= 1; i--)
        drzewo[i] = min(drzewo[2 * i], drzewo[2 * i + 1]);

    for (int i = 0; i < q; i++){
        int typ, a, b, c;
        cin >> typ;
        if (typ == 2){
            cin >> a >> b >> c;
            dodaj(1, 0, R - 1, a - 1, b - 1, c);
        } else {
            cin >> a >> b;
            cout << minimum(1, 0, R - 1, a - 1, b - 1) << endl;
        }
    }
    return 0;
}

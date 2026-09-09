#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int R = (1 << 16);
ll drzewo[R * 2];
ll przep[R * 2];

void przepchnij(int akt_wie, int l, int r){
    przep[l] += przep[akt_wie];
    przep[r] += przep[akt_wie];

    drzewo[l] += przep[akt_wie];
    drzewo[r] += przep[akt_wie];

    przep[akt_wie] = (ll)0;
}

void zmien(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt, ll val){
    if (pocz_odp > kon_pyt || kon_odp < pocz_pyt) {
        return;
    } else if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        drzewo[akt_wie] += val;
        przep[akt_wie] += val;
    } else {
        int l, r, srodek;
        l = akt_wie * 2;
        r = akt_wie * 2 + 1;
        srodek = (pocz_odp + kon_odp) / 2;
        przepchnij(akt_wie, l, r);
        zmien(l, pocz_odp, srodek, pocz_pyt, kon_pyt, val);
        zmien(r, srodek + 1, kon_odp, pocz_pyt, kon_pyt, val);
        drzewo[akt_wie] = max(drzewo[l], drzewo[r]);
    }
}

ll odpowiedz(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt) {
    if (pocz_odp > kon_pyt || kon_odp < pocz_pyt) {
        return 0;
    } else if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        return drzewo[akt_wie];
    } else {
        int l, r, srodek;
        l = akt_wie * 2;
        r = akt_wie * 2 + 1;
        srodek = (pocz_odp + kon_odp) / 2;
        przepchnij(akt_wie, l, r);
        return max(odpowiedz(l, pocz_odp, srodek, pocz_pyt, kon_pyt),
                   odpowiedz(r, srodek + 1, kon_odp, pocz_pyt, kon_pyt));
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m, q;
    cin >> n >> m >> q;

    for (int i = 0; i < q; i++){
        ll a, b, ile;
        cin >> a >> b >> ile;
        b--;
        ll maxi = odpowiedz(1, 0, R - 1, a, b);
        if (maxi + ile > m){
            cout << "N" << endl;
        } else {
            zmien(1, 0, R - 1, a, b, ile);
            cout << "T" << endl;
        }
    }

    return 0;
}

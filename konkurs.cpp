#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int R = (1<<21);
ll drzewo[R * 2];

void zmien(int a, ll x){
    a += R;
    drzewo[a] = x;
    while (a > 1){
        a /= 2;
        drzewo[a] = drzewo[a * 2] + drzewo[a * 2 + 1];
    }
}

ll odp(int pocz_pyt, int kon_pyt, int pocz_odp, int kon_odp, int akt_wie){
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        return drzewo[akt_wie];
    }
    if (kon_pyt < pocz_odp || pocz_pyt > kon_odp){
        return 0;
    }
    int srodek = (pocz_odp + kon_odp) / 2;
    return odp(pocz_pyt, kon_pyt, pocz_odp, srodek, akt_wie * 2) +
    odp(pocz_pyt, kon_pyt, srodek + 1, kon_odp, akt_wie * 2 + 1);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = n; i < R; i++) {
        drzewo[i + R] = 0;
    }

    for (int i = 0; i < n; i++){
        cin >> drzewo[i + R];
    }

    for (int i = R - 1; i >= 1; i--){
        drzewo[i] = drzewo[2 * i] + drzewo[2 * i + 1];
    }

    int q;
    cin >> q;
    while (q--){
        int typ;
        cin >> typ;
        if (typ == 1) {
            int a;
            cin >> a;
            ll ile;
            cin >> ile;
            zmien(a - 1, ile);
        } else {
            ll ile;
            cin >> ile;

            if (drzewo[1] < ile){
                cout << -1 << '\n';
                continue;
            }

            int akt_wie = 1;
            int pocz_odp = 0, kon_odp = R - 1;
            ll mamy = 0;
            while (pocz_odp != kon_odp){
                int srodek = (pocz_odp + kon_odp) / 2;
                ll na_lewo = drzewo[2 * akt_wie];
                if (mamy + na_lewo >= ile){
                    akt_wie *= 2;
                    kon_odp = srodek;
                } else {
                    mamy += na_lewo;
                    akt_wie *= 2;
                    akt_wie++;
                    pocz_odp = srodek + 1;
                }
            }
            if (pocz_odp >= n){
                cout << -1 << '\n';
            } else {
                cout << pocz_odp + 1 << '\n';
            }
        }
    }

    return 0;
}

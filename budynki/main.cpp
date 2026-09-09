#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1e5 + 5;
const int R = (1<<20);
int trojki[R * 2];
int bloki[MAXN];

bool czy_wkurza(int pier, int dru, int trze){
    return (pier < dru && dru > trze && pier < trze);
}

void zmien(int akt_wie, int val){
    trojki[akt_wie] = val;
    while (akt_wie != 1){
        akt_wie /= 2;
        trojki[akt_wie] = trojki[2 * akt_wie] + trojki[2 * akt_wie + 1];
    }
}

ll suma(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt){
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt)
        return trojki[akt_wie];

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt)
        return 0;

    int srodek = (pocz_odp + kon_odp) / 2;
    return suma(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt) +
           suma(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt);
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;

    for (int i = 0; i < n; i++){
        cin >> bloki[i];
    }

    for (int i = 0; i < n - 2; i++){
        int pier = bloki[i];
        int dru = bloki[i + 1];
        int trze = bloki[i + 2];
        if (czy_wkurza(pier, dru, trze)){
            trojki[i] = 1;
        }
    }

    for (int i = R - 1; i >= 1; i--){
        trojki[i] = trojki[i * 2] + trojki[i * 2 + 1];
    }

    while (q--){
        int typ;
        int a, b;
        cin >> typ >> a >> b;
        a--;
        b--;
        if (typ == 2){
            bloki[a] = b;
            if (a != 0){
                bool czy_tak = czy_wkurza(bloki[a - 2], bloki[a - 1], bloki[a]);
                if (czy_tak){
                    zmien(R + a - 2, 1);
                }
            }
            if (a != n - 1){
                bool czy_tak = czy_wkurza(bloki[a], bloki[a + 1], bloki[a + 2]);
                if (czy_tak){
                    zmien(R + a + 2, 1);
                }
            }
            if (a != 0 && a != n - 1){
                bool czy_tak = czy_wkurza(bloki[a - 1], bloki[a], bloki[a + 1]);
                if (czy_tak){
                    zmien(R + a - 1, 1);
                }
            }
        } else {
            cout << suma(1, 0, R - 1, a - 2, b - 2) << '\n';
        }
    }

    return 0;
}

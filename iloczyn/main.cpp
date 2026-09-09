//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/ilo/
#include <iostream>
using namespace std;

const int R = (1 << 21);
const int MOD = 12345;
long long drzewo[2 * R];

void zamiana(int akt_wie, int val){
    drzewo[akt_wie] = val;
    while (akt_wie > 1){
        akt_wie /= 2;
        drzewo[akt_wie] = (drzewo[akt_wie * 2] * drzewo[akt_wie * 2 + 1]) % MOD;
    }
}

long long iloczyn(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt){
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        return drzewo[akt_wie];
    }

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt){
        return 1;
    }

    int srodek = (pocz_odp + kon_odp) / 2;
    return (iloczyn(akt_wie * 2, pocz_odp, srodek, pocz_pyt, kon_pyt) *
        iloczyn(akt_wie * 2 + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt)) % MOD;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < R * 2; i++){
        drzewo[i] = 1;
    }

    int n, q;
    cin >> n >> q;

    for (int i = 0; i < n; i++){
        cin >> drzewo[i + R];
    }

    for (int i = R - 1; i > 0; i--){
        drzewo[i] = (drzewo[i * 2] * drzewo[i * 2 + 1]) % MOD;
    }

    for (int i = 0; i < q; i++){
        int co, a, b;
        cin >> co >> a >> b;
        if (co == 1){
            zamiana(a - 1 + R, b);
        } else {
            cout << iloczyn(1, 0, R - 1, a - 1, b - 1) << '\n';
        }
    }

    return 0;
}

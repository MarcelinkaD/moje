//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/max/
//drzewo przedzialowe przedzial-punkt
#include <iostream>
using namespace std;

const int R = (1 << 20);
long long drzewo[2 * R];

void zmiana(int a){
    drzewo[a] += 1;

    while (a > 1){
        a /= 2;
        drzewo[a] = drzewo[a * 2] + drzewo[a * 2 + 1];
    }
}

long long suma(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt){
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        return drzewo[akt_wie];
    }

    if (kon_odp < pocz_pyt || pocz_odp > kon_pyt) {
        return 0;
    }

    int srodek = (pocz_odp + kon_odp) / 2;
    return suma(2 * akt_wie, pocz_odp, srodek, pocz_pyt, kon_pyt)+
        suma(2 * akt_wie + 1, srodek + 1, kon_odp, pocz_pyt, kon_pyt);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, q;
    cin >> n >> q;

    for (int k = 0; k < q; k++){
        int typ, a, b;
        cin >> typ;
        if (typ == 1){
            cin >> a;
            zmiana(a + R - 1);
        } else {
            cin >> a >> b;
            cout << suma(1, 0, R - 1, a - 1, b - 1) << endl;
        }
    }

    return 0;
}

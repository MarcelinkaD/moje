#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int R = (1 << 20);
//const int R = 8;
ll drzewo[R * 2];

void zmien(int akt_wie, ll var){
    akt_wie += R - 1;
    drzewo[akt_wie] = var;
    while (akt_wie != 0){
        akt_wie /= 2;
        drzewo[akt_wie] = drzewo[akt_wie * 2] + drzewo[akt_wie * 2 + 1];
    }
}

ll odpowiedz(int akt_wie, int szukam){
    ll mniejsze = 0;
    while (akt_wie < R){
        ll na_lewo = drzewo[akt_wie * 2];
        ll na_prawo = drzewo[akt_wie * 2 + 1];
        if (szukam <= mniejsze + na_lewo) {
            akt_wie *= 2;
        } else {
            akt_wie *= 2;
            akt_wie += 1;
            mniejsze += na_lewo;
        }
    }
    return akt_wie - R + 1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;

    for (int i = 0; i < q; i++){
        int t, x;
        cin >> t >> x;
        if (t == 1){
            zmien(x, 1);
        } else if (t == 2){
            zmien(x, 0);
        } else {
            cout << odpowiedz(1, x) << endl;
        }
    }

    return 0;
}

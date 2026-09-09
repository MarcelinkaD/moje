#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MOD = 1e9 + 7;
const int R = (1 << 20);
ll drzewo[R * 2];

void zmien(int a, int b, ll c){
    a += R - 1;
    b += R + 1;
    while (a / 2 != b / 2){
        if (a % 2 == 0){
            drzewo[a + 1] *= c;
            drzewo[a + 1] %= MOD;
        }
        if (b % 2 == 1){
            drzewo[b - 1] *= c;
            drzewo[b - 1] %= MOD;
        }
        a /= 2;
        b /= 2;
    }
}

ll odpowiedz(int akt_wie){
    akt_wie += R;
    ll wyn = 1;
    while (akt_wie != 0){
        wyn *= drzewo[akt_wie];
        wyn %= MOD;
        akt_wie /= 2;
    }
    return wyn;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < R * 2; i++){
        drzewo[i] = 1;
    }

    int q;
    cin >> q;

    for (int i = 0; i < q; i++){
        int t, a;
        cin >> t >> a;
        if (t == 0){
            int b;
            ll c;
            cin >> b >> c;
            zmien(a, b, c);
        } else {
            cout << odpowiedz(a) << endl;
        }

    }

    return 0;
}

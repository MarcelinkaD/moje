//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r2d/
#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int MAXN = 1e6 + 5;
const int R = (1 << 18);
ll suma_do_akt_dnia[2 * R];
int akt_stan[MAXN];

void zmien(int k, ll u) {
    k += R;
    suma_do_akt_dnia[k] = u;
    while (k > 1) {
        k /= 2;
        suma_do_akt_dnia[k] = suma_do_akt_dnia[2 * k] + suma_do_akt_dnia[2 * k + 1];
    }
}

ll suma(int a, int b) {
    a += R;
    b += R;
    if (a == b) {
        return suma_do_akt_dnia[a];
    }
    ll wynik = suma_do_akt_dnia[a] + suma_do_akt_dnia[b];
    while (a != b - 1) {
        if (a % 2 == 0) {
            wynik += suma_do_akt_dnia[a + 1];
        }
        if (b % 2 == 1) {
            wynik += suma_do_akt_dnia[b - 1];
        }
        a /= 2;
        b /= 2;
    }
    return wynik;
}

void update(ll t, ll akt_dzien, int n) {
    ll roznica = t - akt_dzien;
    for (int i = 1; i <= n; i++) {
        ll akt_war = suma_do_akt_dnia[i + R] + (akt_stan[i] * roznica);
        zmien(i, akt_war);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, q;
    cin >> n >> q;

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        suma_do_akt_dnia[i + R] = x;
        akt_stan[i] = x;
    }

    for (int i = R - 1; i >= 1; i--) {
        suma_do_akt_dnia[i] = suma_do_akt_dnia[2 * i] + suma_do_akt_dnia[2 * i + 1];
    }

    ll akt_dzien = 1;
    for (int k = 0; k < q; k++) {
        char typ;
        cin >> typ;
        if (typ == 'Q'){
            int a, b, t;
            cin >> a >> b >> t;
            if (akt_dzien == t) {
                cout << suma(a, b) << endl;
            } else {
                update(t, akt_dzien, n);
                cout << suma(a, b) << endl;
                akt_dzien = t;
            }
        } else if (typ == 'V'){
            int i, v, t;
            cin >> i >> v >> t;
            if (akt_dzien < t) {
                update(t, akt_dzien, n);
                akt_dzien = t;
            }
            akt_stan[i] = v;
        } else if (typ == 'F') {
            int i, t;
            cin >> i >> t;
            if (akt_dzien < t) {
                update(t, akt_dzien, n);
                akt_dzien = t;
            }
            akt_stan[i] = 0;
            zmien(i, 0);
        } else {
            int i, v, t;
            cin >> i >> v >> t;
            if (akt_dzien < t + 1) {
                update(t + 1, akt_dzien, n);
                akt_dzien = t + 1;
            }
            akt_stan[i] = v;
            zmien(i, v);
        }
    }

    return 0;
}

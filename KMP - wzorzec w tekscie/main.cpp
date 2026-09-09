//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/kmp/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int pod = 31;
const ll MOD = 1e9 + 21;

ll powmod(ll a, ll b, ll mod) {
    ll res = 1;
    while (b) {
        if (b & 1) res = (res * a) % mod;
        a = (a * a) % mod;
        b >>= 1;
    }
    return res;
}

int char_to_val(char c) {
    if ('a' <= c && c <= 'z') return c - 'a' + 1;
    else return c - 'A' + 27;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;

    for (int k = 0; k < q; k++) {
        int n;
        cin >> n;
        string wzor, text;
        cin >> wzor >> text;
        int m = text.size();

        vector<ll> pot(max(m, n) + 1);
        pot[0] = 1;
        for (int i = 1; i <= max(m, n); i++) {
            pot[i] = (pot[i - 1] * pod) % MOD;
        }

        vector<ll> inv_pot(max(m, n) + 1);
        inv_pot[max(m, n)] = powmod(pot[max(m, n)], MOD - 2, MOD);
        for (int i = max(m, n) - 1; i >= 0; i--) {
            inv_pot[i] = (inv_pot[i + 1] * pod) % MOD;
        }

        ll hasz_wzor = 0;
        ll akt_pot = 1;
        for (int i = 0; i < n; i++) {
            hasz_wzor = (hasz_wzor + (akt_pot * char_to_val(wzor[i])) % MOD) % MOD;
            akt_pot = (akt_pot * pod) % MOD;
        }

        vector<ll> hasz_text;
        hasz_text.push_back(char_to_val(text[0]) % MOD);
        akt_pot = pod;
        for (int i = 1; i < m; i++) {
            hasz_text.push_back((hasz_text[i - 1] + (akt_pot * char_to_val(text[i])) % MOD) % MOD);
            akt_pot = (akt_pot * pod) % MOD;
        }

        for (int i = 0; i <= m - n; i++) {
            int pocz = i;
            int kon = i + n;

            ll odc = hasz_text[kon - 1];
            if (pocz > 0) {
                odc = (odc - hasz_text[pocz - 1] + MOD) % MOD;
            }
            ll wyn = (odc * inv_pot[pocz]) % MOD;

            if (wyn == hasz_wzor) {
                cout << pocz << "\n";
            }
        }
    }

    return 0;
}

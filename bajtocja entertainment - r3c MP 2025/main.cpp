//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r3c/
#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int MAXN = 500007;
ll pref[MAXN];
vector<pair<ll, ll>> mozliwe_k;
int w[MAXN];

void wypisz_wyn(int n) {
    cout << "TAK" << endl;
    cout << n << endl;
    for (int i = 0; i < n; i++){
        cout << w[i] << ' ';
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll n;
    cin >> n;

    pref[0] = 0;
    for (int i = 1; i <= n; i++){
        int x;
        cin >> x;
        pref[i] = pref[i - 1] + x;
    }

    ll suma = pref[n];

    if (suma > 0) {
        ll pierw = sqrt(suma);
        for (ll k = 1; k <= min(pierw, n); k++) {
            if (suma % k == 0) {
                ll k2 = suma / k;
                if (k != 1 && k <= n) mozliwe_k.push_back({k, k2});
                if (k2 != 1 && k2 <= n) mozliwe_k.push_back({k2, k});
            }
        }
    } else if (suma < 0) {
        ll pierw = sqrt(-suma);
        for (ll k = 1; k <= min(pierw, n); k++) {
            if (suma % k == 0) {
                ll k2 = -suma / k;
                if (k != 1 && k <= n) mozliwe_k.push_back({k, -k2});
                if (k2 != 1 && k2 <= n) mozliwe_k.push_back({k2, -k});
            }
        }
    } else {
        int ost_ind = 0;
        for (int i = 1; i <= n; i++) {
            ll akt_sum = pref[i] - pref[ost_ind];
            if (akt_sum == 0) {
                ll druga_sum = pref[n] - pref[i];
                if (druga_sum == 0 && i != n) {
                    cout << "TAK" << endl;
                    cout << 2 << endl;
                    cout << i << ' ' << n;
                    return 0;
                }
            }
        }
        cout << "NIE" << endl;
        return 0;
    }

    for (int ind = 0; ind < mozliwe_k.size(); ind++) {
        ll k = mozliwe_k[ind].first;
        ll ile = mozliwe_k[ind].second;
        int ile_odc = 0;
        int ost_ind = 0;
        int ost_ind_w = 0;
        for (int i = 1; i <= n; i++) {
            ll akt_sum = pref[i] - pref[ost_ind];
            if (akt_sum == ile) {
                ile_odc++;
                if (ile_odc > k) break;
                w[ost_ind_w] = i;
                ost_ind = i;
                ost_ind_w++;
            }
        }
        if (ile_odc == k) {
            if (ost_ind != n) {
                ll akt_sum = pref[n] - pref[ost_ind];
                if (akt_sum == 0) {
                    w[ost_ind_w - 1] = n;
                } else {
                    continue;
                }
            }
            wypisz_wyn(ost_ind_w);
            return 0;
        }
    }

    cout << "NIE" << endl;
    return 0;
}



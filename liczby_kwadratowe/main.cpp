//AleMozgi 2024/2025
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1e5;
vector<ll> kwadratowe;

int binary(ll x) {
    int rozmiar_kwa = kwadratowe.size();
    int pocz = 0, kon = rozmiar_kwa - 1;
    while (pocz < kon) {
        int srodek = (pocz + kon) / 2;
        if (kwadratowe[srodek] == x) {
            return srodek;
        } else if (kwadratowe[srodek] < x) {
            pocz = srodek + 1;
        } else {
            kon = srodek;
        }
    }

    vector<int> mozliwe;
    if (pocz > 0){
        mozliwe.push_back(pocz - 1);
    }
    mozliwe.push_back(pocz);
    if (pocz < rozmiar_kwa - 1){
        mozliwe.push_back(pocz + 1);
    }

    ll min_roz = 1e9 + 7;
    int wyn = -1;
    for (int i = 0; i < mozliwe.size(); i++) {
        int ind = mozliwe[i];
        ll roz = abs(kwadratowe[ind] - x);
        if (roz < min_roz) {
            min_roz = roz;
            wyn = ind;
        } else if (roz == min_roz && kwadratowe[ind] < kwadratowe[wyn]) {
            wyn = ind;
        }
    }
    return wyn;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 1; i <= MAXN; i++) {
        ll x = (ll)i * i;
        kwadratowe.push_back(x);
    }

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        ll k;
        cin >> k;
        int gdzie = binary(k);
        cout << kwadratowe[gdzie] << ' ';
    }

    return 0;
}

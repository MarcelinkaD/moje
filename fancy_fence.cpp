#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int MOD = 1000000007;
const int MAXN = 100000 + 7;
stack<pair<pair<ll, ll>, ll>> s;
ll akt_wyn = 0;

ll wys[MAXN];
ll szer[MAXN];

ll dodaj(ll h, ll W){
    ll w = W;
    while (!s.empty() && s.top().first.first >= h){
        akt_wyn = (akt_wyn - s.top().second + MOD) % MOD;
        w = (w + s.top().first.second) % MOD;
        s.pop();
    }

    ll wyn = akt_wyn;

    ll war = (((h * (h + 1) / 2) % MOD) * w) % MOD;
    s.push({{h, w}, war});
    akt_wyn = (akt_wyn + war) % MOD;
    
    return (((h * (h + 1) / 2) % MOD) * (w - W + MOD) + wyn) % MOD;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++){
        cin >> wys[i];
    }
    for (int i = 1; i <= n; i++){
        cin >> szer[i];
    }

    ll wyn = 0;
    for (int i = 1; i <= n; i++){
        ll war = dodaj(wys[i], szer[i]);
        wyn = (wyn + szer[i] * war) % MOD;
        war = ((szer[i] * (szer[i] + 1) / 2) % MOD) * ((wys[i] * (wys[i] + 1) / 2) % MOD);
        wyn = (wyn + war) % MOD;
    }
    cout << wyn << '\n';

    return 0;
}
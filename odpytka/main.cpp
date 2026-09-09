#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const ll B = 60;
vector<ll> jp[B]; //jp[B][ktory w ciagu]

ll f(ll x, ll m, ll c){
    return (x * x + c) % m;
}

ll gdzie_wyladuje(ll akt_wie, ll skok) {
    for (ll j = 0; j < B; j++){
        if (skok & (1LL << j)){
            akt_wie = jp[j][akt_wie];
        }
    }
    return akt_wie;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ll m, c, q;
    cin >> m >> c >> q;

    for (ll i = 0; i < B; i++){
        jp[i].resize(m + 1);
    }

    for (ll i = 0; i < m; i++){
        jp[0][i] = f(i, m, c);
    }

    for (ll j = 1; j < B; j++){
        for (ll i = 0; i < m; i++){
            jp[j][i] = jp[j - 1][jp[j - 1][i]];
        }
    }

    for (ll i = 0; i < q; i++){
        ll start;
        ll skoki;
        cin >> start >> skoki;
        ll akt_wierz = gdzie_wyladuje(start, skoki);
        cout << akt_wierz << '\n';
    }

    return 0;
}

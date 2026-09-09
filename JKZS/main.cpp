#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const ll MAXN = 1e5 + 5;
//const ll MAXN = 7;
const ll MAXK = 9;
//const ll MAXK = 4;
const ll INF = LLONG_MAX;
vector<pair<ll, ll>> graf[MAXN];
ll odl[MAXN][MAXK];
bool odw[MAXN][MAXK];
priority_queue<pair<ll, pair<ll, ll>>> kol; // odl, wierz, mod

void dijkstra(ll pocz, ll k){
    odl[pocz][0] = 0;
    kol.push({0, {1, 0}});

    while (!kol.empty()){
        ll u = kol.top().second.first;
        ll akt_droga = -kol.top().first;
        ll mod = kol.top().second.second;
        kol.pop();

        if (odw[u][mod]){
            continue;
        }

        odw[u][mod] = 1;
        odl[u][mod] = akt_droga;
        for (auto wierz : graf[u]){
            ll sasiad = wierz.first;
            ll droga = wierz.second;
            ll n_mod = (mod + 1) % k;
            if (odw[sasiad][n_mod]){
                continue;
            }
            kol.push({-(akt_droga + droga), {sasiad, n_mod}});
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    for (ll i = 0; i < MAXN; i++){
        for (ll j = 0; j < MAXK; j++) {
            odl[i][j] = INF;
            odw[i][j] = 0;
        }
    }

    ll n, m, k;
    cin >> n >> m >> k;

    for (ll i = 0; i < m; i++){
        ll a, b, c;
        cin >> a >> b >> c;
        graf[a].push_back({b, c});
        graf[b].push_back({a, c});
    }

    dijkstra(1, k);
    if (odl[n][0] == INF){
        cout << "NIE" << '\n';
        return 0;
    }
    cout << odl[n][0] << '\n';

    return 0;
}

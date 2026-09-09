#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 5e5 + 5;
const ll INF = LLONG_MAX;
vector<pair<int, ll>> graf[MAXN];
ll odl[MAXN];
priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> kol;

void dijkstra(int start){
    odl[start] = 0;
    kol.push({0, start});

    while (!kol.empty()){
        int akt_wie = kol.top().second;
        ll akt_droga = odl[akt_wie];
        kol.pop();
        for (auto wierz : graf[akt_wie]){
            int sasiad = wierz.first;
            ll droga = wierz.second;
            if (odl[sasiad] > akt_droga + droga){
                odl[sasiad] = odl[akt_wie] + droga;
                kol.push({odl[sasiad], sasiad});
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < MAXN; i++){
        odl[i] = INF;
    }

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++){
        int a, b;
        ll c;
        cin >> a >> b >> c;
        graf[a].push_back({b, c});
        graf[b].push_back({a, c});
    }

    dijkstra(1);

    for (int i = 1; i <= n; i++){
        if (odl[i] == INF){
            cout << -1 << '\n';
        } else {
            cout << odl[i] << '\n';
        }
    }

    return 0;
}

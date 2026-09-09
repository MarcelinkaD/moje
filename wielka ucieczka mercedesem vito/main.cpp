#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 100005;
const ll INF = 1e18;
vector<pair<int, ll>> graf[MAXN];
priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> kol;
ll odl[MAXN];
vector<int> graf_droga[MAXN];
vector<int> sciezka;

void Dijkstra(int od) {
    odl[od] = 0;
    kol.push({0, 1});
    while (!kol.empty()){
        int u = kol.top().second;
        kol.pop();
        for (int i = 0; i < graf[u].size(); i++){
            int sasiad = graf[u][i].first;
            ll droga = graf[u][i].second;
            if (odl[sasiad] > odl[u] + droga) {
                odl[sasiad] = odl[u] + droga;
                graf_droga[sasiad].clear();
                graf_droga[sasiad].push_back(u);
                kol.push({odl[sasiad], sasiad});
            } else if (odl[sasiad] == odl[u] + droga) {
                odl[sasiad] = odl[u] + droga;
                graf_droga[sasiad].push_back(u);
                kol.push({odl[sasiad], sasiad});
            }
        }
    }
}

void dfs(int akt_wie){
    odl[akt_wie] = 1;
    for (auto sasiad : graf_droga[akt_wie]){
        if (odl[sasiad] == INF){
            sciezka.push_back(sasiad);
            dfs(sasiad);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < MAXN; i++){
        odl[i] = INF;
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        ll s;
        cin >> a >> b >> s;
        graf[a].push_back({b, s});
        graf[b].push_back({a, s});
    }

    Dijkstra(1);
    for (int i = 0; i < MAXN; i++){
        odl[i] = INF;
    }

    sciezka.push_back(n);
    dfs(n);

    sort(sciezka.begin(), sciezka.end());

    for (auto i : sciezka) {
        cout << i << '\n';
    }

    return 0;
}

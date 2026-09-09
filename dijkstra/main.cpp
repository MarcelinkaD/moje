#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;
const long long INF = 1e18;
vector<pair<int, long long>> graf[MAXN];
priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> kol;
long long odl[MAXN];
int poprzedni[MAXN];
vector<int> sciezka;

void Dijkstra(int od, int kon) {
    odl[od] = 0;
    kol.push({0, 1});

    while (!kol.empty()){
        int u = kol.top().second;
        kol.pop();

        for (int i = 0; i < graf[u].size(); i++){
            int sasiad = graf[u][i].first;
            long long droga = graf[u][i].second;
            if (odl[sasiad] > odl[u] + droga) {
                odl[sasiad] = odl[u] + droga;
                poprzedni[sasiad] = u;
                kol.push({odl[sasiad], sasiad});
            }
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

    for (int i = 0; i < m; i++) {
        int a, b;
        long long s;
        cin >> a >> b >> s;
        graf[a].push_back({b, s});
        graf[b].push_back({a, s});
    }

    for (int i = 1; i <= n; i++){
        odl[i] = INF;
    }

    Dijkstra(1, n);
    if (odl[n] == INF) {
        cout << "NIE" << endl;
        return 0;
    }

    int odl_sciezki = 0;
    int akt_wie = n;

    while (akt_wie != 1) {
        odl_sciezki++;
        sciezka.push_back(akt_wie);
        akt_wie = poprzedni[akt_wie];
    }

    sciezka.push_back(1);
    cout << odl_sciezki << endl;

    for (int i = odl_sciezki; i >= 0; i--) {
        cout << sciezka[i] << ' ';
    }

    return 0;
}

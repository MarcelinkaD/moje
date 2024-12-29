//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/dij1/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAXN = 1000005;
const int INF = 1000005;
vector<pair<int, int>> graf[MAXN];
int odl[MAXN];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> kol;

void dijkstra(int od) {
    odl[od] = 0;
    kol.push({0, od});

    while(!kol.empty()){
        int akt_wie = kol.top().second;
        int akt_odl = kol.top().first;
        kol.pop();

        for (int i = 0; i < graf[akt_wie].size(); i++) {
            int sasiad = graf[akt_wie][i].first;
            int droga = graf[akt_wie][i].second;
            if (odl[sasiad] > akt_odl + droga) {
                odl[sasiad] = akt_odl + droga;
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
        int a, b, c;
        cin >> a >> b >> c;
        graf[a].push_back({b, c});
        graf[b].push_back({a, c});
    }

    for (int i = 1; i <= n; i++) {
        odl[i] = INF;
    }

    dijkstra(1);

    if (odl[n] == INF) {
        cout << -1 << endl;
    } else {
        cout << odl[n] << endl;
    }

    return 0;
}

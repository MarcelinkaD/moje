//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/jes/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1e5 + 5;
const ll INF = 1e15 + 5;
vector<pair<int, int>> graf[MAXN];
pair<ll, int> odl[MAXN];
priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> kol;
vector<int> wyn;

void dijkstra(int od){
    odl[od].first = 0;
    odl[od].second = -1;
    kol.push({0, od});

    while (!kol.empty()){
        int akt_wie = kol.top().second;
        ll akt_odl = kol.top().first;
        kol.pop();

        for (int i = 0; i < graf[akt_wie].size(); i++) {
            int sasiad = graf[akt_wie][i].first;
            int droga = graf[akt_wie][i].second;
            if (odl[sasiad].first > akt_odl + droga) {
                odl[sasiad].first = akt_odl + droga;
                odl[sasiad].second = akt_wie;
                kol.push({odl[sasiad].first, sasiad});
            } else if (odl[sasiad].first == akt_odl + droga && akt_wie < odl[sasiad].second) {
                odl[sasiad].second = akt_wie;
                kol.push({odl[sasiad].first, sasiad});
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        graf[a].push_back({b, c});
        graf[b].push_back({a, c});
    }

    for (int i = 0; i < MAXN; i++){
        odl[i].first = INF;
    }

    dijkstra(1);

    if (odl[n].first == INF){
        cout << -1 << endl;
        return 0;
    } else {
        int akt_wie = n;
        while (akt_wie != -1){
            wyn.push_back(akt_wie);
            akt_wie = odl[akt_wie].second;
        }
    }

    reverse(wyn.begin(), wyn.end());
    cout << wyn.size() << endl;
    for (int i = 0; i < wyn.size(); i++){
        cout << wyn[i] << ' ';
    }

    return 0;
}

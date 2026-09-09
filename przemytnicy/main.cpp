#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 5005;
const ll INF = LLONG_MAX;
vector<pair<int, ll>> graf_NORM[MAXN];
vector<pair<int, ll>> graf_NIENORM[MAXN];
ll odl_NORM[MAXN];
ll odl_NIENORM[MAXN];
int ceny[MAXN];
priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> KOLEJKA;

void dijkstra_NORMALNA(int start){
    odl_NORM[start] = 0;
    KOLEJKA.push({0, start});

    while (!KOLEJKA.empty()){
        int akt_wie = KOLEJKA.top().second;
        ll akt_droga = odl_NORM[akt_wie];
        KOLEJKA.pop();
        for (auto wierz : graf_NORM[akt_wie]){
            int sasiad = wierz.first;
            ll droga = wierz.second;
            if (odl_NORM[sasiad] > akt_droga + droga){
                odl_NORM[sasiad] = odl_NORM[akt_wie] + droga;
                KOLEJKA.push({odl_NORM[sasiad], sasiad});
            }
        }
    }
}

void dijkstra_NIENORMALNA(int start){
    odl_NIENORM[start] = 0;
    KOLEJKA.push({0, start});

    while (!KOLEJKA.empty()){
        int akt_wie = KOLEJKA.top().second;
        ll akt_droga = odl_NIENORM[akt_wie];
        KOLEJKA.pop();
        for (auto wierz : graf_NIENORM[akt_wie]){
            int sasiad = wierz.first;
            ll droga = wierz.second;
            if (odl_NIENORM[sasiad] > akt_droga + droga){
                odl_NIENORM[sasiad] = odl_NIENORM[akt_wie] + droga;
                KOLEJKA.push({odl_NIENORM[sasiad], sasiad});
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < MAXN; i++){
        odl_NORM[i] = INF;
        odl_NIENORM[i] = INF;
    }

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        ceny[i + 1] = x;
    }

    int m;
    cin >> m;

    for (int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        graf_NORM[a].push_back({b, c});
        graf_NIENORM[b].push_back({a, c});
    }

    dijkstra_NIENORMALNA(1);
    dijkstra_NORMALNA(1);

    ll naj_wyn = INF;
    for (int i = 1; i <= n; i++){
        if (odl_NIENORM[i] == INF || odl_NORM[i] == INF){
            continue;
        }
        ll akt_wyn = odl_NORM[i] * 2 + odl_NIENORM[i] * 2 + ceny[i];
        naj_wyn = min(naj_wyn, akt_wyn);
    }
    cout << naj_wyn / 2 << '\n';

    return 0;
}

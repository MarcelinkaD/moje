#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

struct kraw {
    int wierz;
    ll droga;
};

vector<vector<kraw>> graf;
vector<ll> odl;

void dijkstra(int start){
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> kol;
    odl[start] = 0;
    kol.push({0, start});

    while (!kol.empty()){
        int wierz = kol.top().second;
        kol.pop();

        for (auto sasiad : graf[wierz]){
            ll trasa = sasiad.droga;
            if (odl[sasiad.wierz] > odl[wierz] + trasa){
                odl[sasiad.wierz] = odl[wierz] + trasa;
                kol.push({odl[sasiad.wierz], sasiad.wierz});
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    vector<ll> koszt(n + 1);
    graf.resize(n + 1);
    ll INF = LLONG_MAX;
    odl.resize(n + 1, INF);

    for (int i = 1; i <= n; i++){
        cin >> koszt[i];
    }

    for (int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        kraw k1, k2;
        k1.droga = koszt[b];
        k1.wierz = b;
        k2.droga = koszt[a];
        k2.wierz = a;
        graf[a].push_back(k1);
        graf[b].push_back(k2);
    }

    dijkstra(1);

    cout << odl[n] << '\n';

    return 0;
}
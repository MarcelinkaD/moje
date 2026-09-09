#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

struct kraw {
    int wierz, kolor;
    ll koszt, koszt_przem;
};

vector<vector<kraw>> graf;
vector<ll> odl;

void ustaw_koszt(int akt_wie){
    unordered_map<ll, pair<ll, int>> kolory;
    
    for (auto sasiad : graf[akt_wie]){
        kolory[sasiad.kolor].first += sasiad.koszt_przem;
        kolory[sasiad.kolor].second++;
    }

    for (auto &sasiad : graf[akt_wie]){
        if (kolory[sasiad.kolor].second == 1){
            sasiad.koszt = 0;
        } else {
            sasiad.koszt = min(sasiad.koszt_przem, kolory[sasiad.kolor].first - sasiad.koszt_przem);
        }
    }
}

void dijkstra(int start){
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> kol;
    odl[start] = 0;
    kol.push({0, start});

    while (!kol.empty()){
        int wierz = kol.top().second;
        kol.pop();

        for (auto sasiad : graf[wierz]){
            ll trasa = sasiad.koszt;
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

    int n, m, start, kon;
    cin >> n >> m >> start >> kon;
    graf.resize(n + 1);
    odl.resize(n + 1);

    for (int i = 0; i < m; i++){
        int a, b, kol, koszt;
        cin >> a >> b >> kol >> koszt;
        kraw k;
        k.wierz = b;
        k.kolor = kol;
        k.koszt_przem = koszt;
        k.koszt = 0;
        graf[a].push_back(k);
    }

    for (int i = 1; i <= n; i++){
        ustaw_koszt(i);
        odl[i] = LLONG_MAX;
    }

    dijkstra(start);

    if (odl[kon] == LLONG_MAX){
        cout << -1 << '\n';
    } else {
        cout << odl[kon] << '\n';
    }

    return 0;
}
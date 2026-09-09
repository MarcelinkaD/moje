#include <bits/stdc++.h>
using namespace std;

priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> kol;

void dijkstra(int od, ) {
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

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<vector<pair<int, int>>> graf(n);

    for (int i = 1; i <= n; i++){
        int wag, ile;
        cin >> wag >> ile;
        for (int k = 0; k < ile; k++){
            int x;
            cin >> x;
            graf[x].push_back({i, wag});
        }
    }



    return 0;
}
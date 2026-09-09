#include <bits/stdc++.h>
using namespace std;

struct dziura{
    bool odw = 0;
    vector<pair<int, int>> sciezki;
    int wysokosc = INT_MAX;
};

vector<dziura> graf;

void dfs(int komora, int min_wys){
    graf[komora].odw = true;
    graf[komora].wysokosc = min_wys;

    for(auto &sasiad : graf[komora].sciezki){
        int v = sasiad.first;
        int w = sasiad.second;
        if(!graf[v].odw){
            dfs(v, min(min_wys, w));
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;

    while(q--){
        int n, k;
        cin >> n >> k;

        graf.clear();
        graf.resize(n+1);

        for(int i = 1; i < n; i++){
            int a, b, c; cin >> a >> b >> c;
            graf[a].sciezki.push_back({b,c});
            graf[b].sciezki.push_back({a,c});
        }

        int m; cin >> m;
        vector<int> gornicy(m);
        for(int i = 0; i < m; i++){
            cin >> gornicy[i];
        }

        dfs(k, INT_MAX);

        vector<int> min_wys;
        for(int i = 1; i <= n; i++){
            if(i == k) continue;
            if(graf[i].sciezki.size() == 1){
                min_wys.push_back(graf[i].wysokosc);
            }
        }

        sort(gornicy.begin(), gornicy.end());
        sort(min_wys.begin(), min_wys.end());

        int w = 0;
        int i = 0, j = 0;
        while(i < (int)gornicy.size() && j < (int)min_wys.size()){
            if(gornicy[i] <= min_wys[j]){
                w++;
                i++;
                j++;
            } else {
                j++;
            }
        }

        cout << w << "\n";
    }

    return 0;
}

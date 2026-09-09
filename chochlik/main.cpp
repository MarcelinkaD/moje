#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e5 + 5;
//const int MAXN = 5;

bool sprawdz(int start, vector<vector<pair<int, bool>>> &graf, vector<pair<bool, bool>> &odw){
    queue<pair<int, bool>> kol;
    odw[start].first = true;
    kol.push({start, 0});
    while (!kol.empty()){
        pair<int, bool> u = kol.front();
        kol.pop();

        if (odw[u.first].first && odw[u.first].second) {
            return false;
        }

        for (auto sasiad : graf[u.first]){
            int now_wie = sasiad.first;
            bool typ = sasiad.second;
            if (typ == 0){
                if (u.second == 0){
                    if (!odw[now_wie].first){
                        odw[now_wie].first = true;
                        kol.push({now_wie, 0});
                    }
                } else {
                    if (!odw[now_wie].second){
                        odw[now_wie].second = true;
                        kol.push({now_wie, 1});
                    }
                }
            } else {
                if (u.second == 0){
                    if (!odw[now_wie].second){
                        odw[now_wie].second = true;
                        kol.push({now_wie, 1});
                    }
                } else {
                    if (!odw[now_wie].first){
                        odw[now_wie].first = true;
                        kol.push({now_wie, 0});
                    }
                }
            }
        }
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;

    while(q--){
        int n, m;
        cin >> n >> m;
        vector<vector<pair<int, bool>>> graf(n + 1);
        vector<pair<bool, bool>> odw(n + 1, {0, 0}); //w prawo 0, w lewo 1
        for (int i = 0; i < m; i++){
            int a, b;
            char typ;
            cin >> a >> b >> typ;
            if (typ == 'A'){
                graf[a].push_back({b, 0});
                graf[b].push_back({a, 0});
            } else {
                graf[a].push_back({b, 1});
                graf[b].push_back({a, 1});
            }
        }
        bool wyn = true;
        for (int i = 1; i <= n; i++){
            if (odw[i].first == 0 && odw[i].second == 0){
                wyn = sprawdz(i, graf, odw);
                if (wyn == 0){
                    cout << "NIE" << '\n';
                    break;
                }
            }
        }

        if (wyn){
            cout << "TAK" << '\n';
        }
    }

    return 0;
}

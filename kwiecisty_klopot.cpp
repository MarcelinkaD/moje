#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

vector<bool> gdzie_kwia;
vector<vector<int>> graf;
vector<bool> czy_odw;
vector<int> ojciec;

void dfs(int akt_wie){
    czy_odw[akt_wie] = true;
    for (auto sasiad : graf[akt_wie]){
        if (!czy_odw[sasiad]){
            ojciec[sasiad] = akt_wie;
            dfs(sasiad);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    graf.resize(n + 1);
    gdzie_kwia.resize(n + 1);
    czy_odw.resize(n + 1);
    ojciec.resize(n + 1);

    for (int i = 0; i < k; i++){
        int x;
        cin >> x;
        gdzie_kwia[x] = true;
    }

    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    ojciec[1] = 0;
    dfs(1);
    for (int i = 1; i <= n; i++){
        bool czy_byl = 0;
        int akt_wie = i;
        while (akt_wie != 0){
            if (gdzie_kwia[akt_wie]) {
                czy_byl = true;
                break;
            }
            akt_wie = ojciec[akt_wie];
        }
        if (czy_byl){
            cout << i << ' ';
        }
    }

    return 0;
}
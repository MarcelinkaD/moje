#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 30005;
const int L = 20;
vector<vector<int>> graf;
vector<bool> odw;
vector<ll> glebokosc;
int ojciec[MAXN][L];

void ustaw(int akt_wie, int akt_gle){
    odw[akt_wie] = true;
    glebokosc[akt_wie] = akt_gle;
    for (auto i : graf[akt_wie]){
        if (!odw[i]){
            ojciec[i][0] = akt_wie;
            ustaw(i, akt_gle + 1);
        }
    }
}

int lca(int u, int v){
    if (glebokosc[u] > glebokosc[v]){
        swap(u, v);
    }

    for (int i = L - 1; i >= 0; i--){
        if (glebokosc[ojciec[v][i]] >= glebokosc[u]){
            v = ojciec[v][i];
        }
    }

    if (u == v){
        return u;
    }

    for (int i = L - 1; i >= 0; i--){
        if (ojciec[v][i] != ojciec[u][i]){
            v = ojciec[v][i];
            u = ojciec[u][i];
        }
    }

    return ojciec[v][0];
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    graf.resize(n + 1);
    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    glebokosc.resize(n + 1);
    odw.resize(n + 1);
    glebokosc[1] = 0;
    odw[1] = true;
    ojciec[1][0] = 1;
    ustaw(1, 0);

    for (int j = 1; j < L; j++){
        for (int i = 1; i <= n; i++){
            ojciec[i][j] = ojciec[ojciec[i][j - 1]][j - 1];
            if (ojciec[i][j] == 0){
                ojciec[i][j] = 1;
            }
        }
    }

    int q;
    cin >> q;
    int w = 0;
    int akt_wie = 1;
    for (int i = 0; i < q; i++){
        int v;
        cin >> v;

        if (akt_wie == 1){
            w += glebokosc[v];
        } else {
            int lc = lca(akt_wie, v);
            w += glebokosc[akt_wie];
            w += glebokosc[v];
            w -= glebokosc[lc] * 2;
        }
        akt_wie = v;
    }
    cout << w << '\n';
    return 0;
}

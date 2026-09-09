#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2e5 + 5;
const int INF = INT_MAX;
vector<int> graf[MAXN];
int odl[MAXN];

void bfs(int akt_wie){
    queue<int> kol;
    kol.push(akt_wie);

    while (!kol.empty()){
        int u = kol.front();
        kol.pop();
        for (auto sasiad : graf[u]){
            if (odl[sasiad] == INF){
                odl[sasiad] = odl[u] + 1;
                kol.push(sasiad);
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < MAXN; i++){
        odl[i] = INF;
    }

    int n, m;
    cin >> n >> m;
    odl[1] = 0;

    for (int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    bfs(1);

    for (int i = 1; i <= n; i++){
        if (odl[i] == INF){
            cout << -1 << '\n';
        } else {
            cout << odl[i] << '\n';
        }
    }

    return 0;
}

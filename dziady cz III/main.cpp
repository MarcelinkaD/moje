#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1e6 + 5;
int odl[MAXN];
bool odw[MAXN];
vector<int> graf[MAXN];
ll ile_dziadow[MAXN];
ll akt_dziady;

ll bfs(ll k){
    queue<int> kol;
    odw[0] = true;
    odl[0] = 0;
    kol.push(0);

    while (!kol.empty()){
        int u = kol.front();
        kol.pop();
        akt_dziady += ile_dziadow[u];
        if (akt_dziady > k){
            return odl[u];
        }
        for (auto sasiad : graf[u]){
            if (!odw[sasiad]){
                odl[sasiad] = odl[u] + 1;
                kol.push(sasiad);
                odw[sasiad] = 1;
            }
        }
    }
    return -1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    ll k;
    cin >> n >> m >> k;

    for (int i = 0; i < n; i++){
        cin >> ile_dziadow[i];
    }

    for (int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        graf[b].push_back(a);
    }

    ll czy_przep = bfs(k);
    if (czy_przep != -1){
        cout << czy_przep << '\n';
    } else {
        cout << "Dziadygga" << '\n';
    }

    return 0;
}

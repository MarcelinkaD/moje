//Implementacja œrednicy: https://cses.fi/problemset/task/1131
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXN = 200005;
const int INF = 1000000;
vector<int> graf[MAXN];
int odl[MAXN];

pair<int, int> BFS(int od) {
    queue<int> kol;
    odl[od] = 0;
    kol.push(od);
    pair<int, int> w;

    while(!kol.empty()){
        int u = kol.front();
        kol.pop();
        for (int i = 0; i < graf[u].size(); i++){
            int sasiad = graf[u][i];
            if (odl[sasiad] == INF) {
                odl[sasiad] = odl[u] + 1;
                if (odl[sasiad] > w.second) {
                    w.first = sasiad;
                    w.second = odl[sasiad];
                }
                kol.push(sasiad);
            }
        }
    }
    return w;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    for (int i = 0; i <= n; i++) {
        odl[i] = INF;
    }

    pair<int, int> w1 = BFS(1);

    for (int i = 0; i <= n; i++) {
        odl[i] = INF;
    }

    pair<int, int> w2 = BFS(w1.first);

    cout << w2.second << endl;

    return 0;
}

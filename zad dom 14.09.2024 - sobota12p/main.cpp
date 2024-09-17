// 1) DFS (implementacja) https://szkopul.edu.pl/problemset/problem/AH7extaluK4eok1ECZF9s2ep/site/?key=statement
/*
#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000004;
vector<int> graf[MAXN];
vector<int> wyn;
bool czy_odw[MAXN];

void dfs(int akt_v) {
    czy_odw[akt_v] = 1;
    wyn.push_back(akt_v);
    for (int i = 0; i < graf[akt_v].size(); i++) {
        int sasiad = graf[akt_v][i];
        if (!czy_odw[sasiad]) {
            dfs(sasiad);
        }
    }
}

int main()
{
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    dfs(1);
    sort(wyn.begin(), wyn.end());

    cout << wyn.size() << endl;

    for (int i = 0; i < wyn.size(); i++) {
        cout << wyn[i] << ' ';
    }

    return 0;
}
*/

// 2) Lista kontaktów (str. 134)
/*
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAXN = 1000004;
vector<int> graf[MAXN];

bool bfs(int pocz, int kon) {
    queue<int> kol;
    kol.push(pocz);

    while (!kol.empty()) {
        int v = kol.front();
        kol.pop();
        for (int i = 0; i < graf[v].size(); i++) {
            if (graf[v][i] != kon) {
                kol.push(graf[v][i]);
            } else {
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
    }

    int q;
    cin >> q;

    for (int i = 0; i < q; i++){
        int x, y;
        cin >> x >> y;

        if (bfs(x, y)) {
            cout << "TAK" << endl;
        } else {
            cout << "NIE" << endl;
        }
    }

    return 0;
}
*/

// 3) https://cses.fi/problemset/task/1192
#include <iostream>
#include <string>
using namespace std;

const int MAXN = 1003;
string graf[MAXN];
bool czy_odw[MAXN][MAXN];
int ruchy[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

bool inRange(int ny, int nx, int n, int m) {
    if ((ny < n && nx < m) && (0 <= ny && 0 <= nx)) {
        return 1;
    }
    return 0;
}

void dfs(int i, int j, int n, int m) {
    czy_odw[i][j] = 1;
    for (int k = 0; k < 4; k++) {
        int ni, nj;
        ni = i + ruchy[k][0];
        nj = j + ruchy[k][1];

        if (!inRange(ni, nj, n, m)) {
            continue;
        }

        if (graf[ni][nj] == '#') {
            continue;
        }

        if (!czy_odw[ni][nj]) {
            dfs(ni, nj, n, m);
        }
    }
}

int main()
{
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string l;
        cin >> l;
        graf[i] = l;
    }

    int w = 0;

    for (int y = 0; y < n; y++) {
        for (int x = 0; x < m; x++) {
            if (!czy_odw[y][x] && graf[y][x] == '.') {
                w++;
                dfs(y, x, n, m);
            }
        }
    }

    cout << w << endl;

    return 0;
}


#include <bits/stdc++.h>
using namespace std;

const int MAXN = 30005;
const int L = 20;
vector<int> graf[MAXN];
vector<int> kol;
int ojciec[MAXN][L];
int glebokosc[MAXN];
bool odw[MAXN];

void dfs(int akt_wie){
    odw[akt_wie] = 1;
    for (auto sasiad : graf[akt_wie]){
        if (!odw[sasiad]){
            glebokosc[sasiad] = glebokosc[akt_wie] + 1;
            ojciec[sasiad][0] = akt_wie;
            dfs(sasiad);
        }
    }
}

int lca(int a, int b){
    if (glebokosc[a] > glebokosc[b]){
        swap(a, b);
    }
    for (int i = L - 1; i >= 0; i--){
        if (glebokosc[ojciec[b][i]] >= glebokosc[a]) {
            b = ojciec[b][i];
        }
    }

    if (a == b){
        return a;
    }

    for (int i = L - 1; i >= 0; i--) {
        if (ojciec[a][i] != ojciec[b][i]) {
            a = ojciec[a][i];
            b = ojciec[b][i];
        }
    }
    return ojciec[b][0];
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    int m;
    cin >> m;

    for (int i = 0; i < m; i++){
        int x;
        cin >> x;
        kol.push_back(x);
    }

    glebokosc[1] = 1;
    ojciec[1][0] = 1;
    dfs(1);

    for (int j = 1; j < L; j++){
        for (int i = 1; i <= n; i++){
            ojciec[i][j] = ojciec[ojciec[i][j - 1]][j - 1];
            if (ojciec[i][j] == 0){
                ojciec[i][j] = 1;
            }
        }
    }

    long long wyn = 0;
    for (int i = 0; i < m - 1; i++){
        int a, b;
        a = kol[i];
        b = kol[i + 1];
        int LCA = lca(a, b);
        long long wyna = glebokosc[a] - glebokosc[LCA];
        long long wynb = glebokosc[b] - glebokosc[LCA];
        wyn += wyna + wynb;
    }

    cout << wyn << '\n';

    return 0;
}

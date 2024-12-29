//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/lca/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
const int L = 20;
vector<int> graf[MAXN];
int ojciec[MAXN][L];
int glebokosc[MAXN];
bool czy_odw[MAXN];

void wyznacz_ojca(int akt_wie) {
    czy_odw[akt_wie] = 1;
    for (int i = 0; i < graf[akt_wie].size(); i++){
        int sasiad = graf[akt_wie][i];
        if (!czy_odw[sasiad]){
            glebokosc[sasiad] = glebokosc[akt_wie] + 1;
            ojciec[sasiad][0] = akt_wie;
            wyznacz_ojca(sasiad);
        }
    }
}

int lca(int u, int v) {
    if (glebokosc[u] > glebokosc[v]) {
        swap(v, u);
    }
    for (int i = L - 1; i >= 0; i--) {
        if (glebokosc[ojciec[v][i]] >= glebokosc[u]) {
            v = ojciec[v][i];
        }
    }

    if (u == v) {
        return u;
    }

    for (int i = L - 1; i >= 0; i--) {
        if (ojciec[u][i] != ojciec[v][i]) {
            u = ojciec[u][i];
            v = ojciec[v][i];
        }
    }
    return ojciec[v][0];
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, korzen, q;
    cin >> n >> korzen >> q;

    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    glebokosc[korzen] = 1;
    ojciec[korzen][0] = korzen;
    wyznacz_ojca(korzen);

    for (int j = 1; j < L; j++){
        for (int i = 1; i <= n; i++){
            ojciec[i][j] = ojciec[ojciec[i][j - 1]][j - 1];
            if (ojciec[i][j] == 0) {
                ojciec[i][j] = korzen;
            }
        }
    }

    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << lca(a, b) << endl;
    }

    return 0;
}

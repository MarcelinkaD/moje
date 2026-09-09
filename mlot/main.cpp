//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/mlo/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
const int L = 21;
vector<int> graf[MAXN];
int ojciec[MAXN][L];
int glebokosc[MAXN];
bool czy_odw[MAXN];

void przydziel_ojca(int akt_wie) {
    czy_odw[akt_wie] = true;
    for (auto sasiad : graf[akt_wie]){
        if (!czy_odw[sasiad]){
            glebokosc[sasiad] = glebokosc[akt_wie] + 1;
            ojciec[sasiad][0] = akt_wie;
            przydziel_ojca(sasiad);
        }
    }
}

int znajdz_ojca(int u, int p) {
    for (int i = 0; i < L; i++) {
        if (p & (1 << i)) {
            u = ojciec[u][i];
            if (u == -1) return -1;
        }
    }
    return u;
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

    glebokosc[1] = 1;
    ojciec[1][0] = -1;
    przydziel_ojca(1);

    for (int j = 1; j < L; j++) {
        for (int i = 1; i <= n; i++) {
            if (ojciec[i][j - 1] != -1)
                ojciec[i][j] = ojciec[ojciec[i][j - 1]][j - 1];
            else
                ojciec[i][j] = -1;
        }
    }

    int q;
    cin >> q;
    while(q--) {
        int u, p;
        cin >> u >> p;
        int wynik = znajdz_ojca(u, p);
        if (wynik == -1) cout << "LUCY\n";
        else cout << wynik << "\n";
    }

    return 0;
}

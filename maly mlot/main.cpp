//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/mal/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
const int L = 21;
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

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

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
    wyznacz_ojca(1);

    for (int j = 1; j < L; j++){
        for (int i = 1; i <= n; i++){
            ojciec[i][j] = ojciec[ojciec[i][j - 1]][j - 1];
            if (ojciec[i][j] == -1) {
                ojciec[i][j] = -1;
            }
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int u, p;
        cin >> u >> p;
        p--;
        if (p < 0 || p >= L) {
            cout << "LUCY" << endl;
            continue;
        }
        if ((1 << p) > (glebokosc[u] - 1)) {
            cout << "LUCY" << endl;
            continue;
        }

        int o = ojciec[u][p];
        if (o == -1) {
            cout << "LUCY" << endl;
        } else {
            cout << o << endl;
        }
    }
}

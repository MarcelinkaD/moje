// https://szkopul.edu.pl/c/oki-poziom-2-202425/p/bfs/
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

const int MAXN = 1000006;
vector<int> graf[MAXN];
bool czy_odw[MAXN];
int odl[MAXN];

void bfs(int od) {
    queue<int> kol = {};
    kol.push(od);
    odl[od] = 0;
    czy_odw[od] = 1;

    while (!kol.empty()) {
        int akt_wie = kol.front();
        kol.pop();
        for (int i = 0; i < graf[akt_wie].size(); i++){
            int sasiad = graf[akt_wie][i];
            if (!czy_odw[sasiad]) {
                czy_odw[sasiad] = 1;
                kol.push(sasiad);
                odl[sasiad] = odl[akt_wie] + 1;
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    bfs(0);
    int wyn = 0;

    for (int i = 0; i <= n; i++) {
        wyn += odl[i] * 2;
    }

    cout << wyn;

    return 0;
}

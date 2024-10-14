// https://szkopul.edu.pl/c/oki-poziom-2-202425/p/zaj/18965/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXN = 1005;
bool czy_odw[MAXN][MAXN];
int odl[MAXN][MAXN];
char graf[MAXN][MAXN];
queue<pair<int, int>> kol;
int ruchy[8][2] = {{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};

bool inRange(int ni, int nj, int n, int m) {
    return ((nj < m && ni < n) && (0 <= nj && 0 <= ni));
}

int bfs(int si, int sj, int n, int m) {
    kol.push(make_pair(si, sj));
    odl[si][sj] = 0;
    czy_odw[si][sj] = 1;

    while (!kol.empty()){
        pair<int, int> u = kol.front();
        kol.pop();
        int i = u.first;
        int j = u.second;

        if (graf[i][j] == 'n') {
            return odl[i][j];
        }

        for (int k = 0; k < 8; k++) {
            int ni = i + ruchy[k][0];
            int nj = j + ruchy[k][1];

            if (inRange(ni, nj, n, m) && !czy_odw[ni][nj] && graf[ni][nj] != 'x'){
                czy_odw[ni][nj] = 1;
                odl[ni][nj] = odl[i][j] + 1;
                kol.push(make_pair(ni, nj));
            }
        }
    }
    return -1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m, si, sj;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++){
            cin >> graf[i][j];
            if (graf[i][j] == 'z'){
                si = i;
                sj = j;
            }
        }
    }

    int wyn = bfs(si, sj, n, m);

    if (wyn == -1) {
        cout << "NIE" << endl;
    } else {
        cout << wyn << endl;
    }

    return 0;
}

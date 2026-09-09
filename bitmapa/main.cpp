//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/bit/34263/
#include <bits/stdc++.h>
using namespace std;

queue<pair<int, int>> kol;
const int MAXN = 182;
const int INF = 1e6;
int bitmapa[MAXN][MAXN];
int odp[MAXN][MAXN];
bool odw[MAXN][MAXN];
pair<int, int> ruchy[4] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

void bfs(int akti, int aktj, int n, int m){
    while (!kol.empty()){
        pair<int, int> wierz = kol.front();
        kol.pop();
        akti = wierz.first;
        aktj = wierz.second;
        for (int i = 0; i < 4; i++){
            pair<int, int> ruch;
            ruch = ruchy[i];
            int ni = akti + ruch.first;
            int nj = aktj + ruch.second;
            if ((0 <= ni && ni < n) && (0 <= nj && nj < m)){
                if (!odw[ni][nj]){
                    odp[ni][nj] = odp[akti][aktj] + 1;
                    odw[ni][nj] = true;
                    kol.push({ni, nj});
                }
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    int si, sj;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            char x;
            cin >> x;
            bitmapa[i][j] = x - '0';
            if (bitmapa[i][j] != 1){
                odp[i][j] = INF;
                odw[i][j] = false;
            } else {
                si = i;
                sj = j;
                odp[i][j] = 0;
                kol.push({si, sj});
                odw[i][j] = true;
            }
        }
    }

    bfs(si, sj, n, m);

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cout << odp[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}

//https://szkopul.edu.pl/c/konkurs-przed-obozem-oki-2025/p/sko/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
char szach[MAXN][MAXN];
int odw[MAXN][MAXN];
pair<int, int> ruchy[8] = {{-2, 1}, {2, -1}, {2, 1}, {-2, -1}, {1, 2}, {-1, 2}, {1, -2}, {-1, -2}};

bool inRange(int akti, int aktk, int n, int m){
    if (akti < 0 || akti > n){
        return false;
    }
    if (aktk < 0 || aktk > m){
        return false;
    }
    return true;
}

void bfs(int akti, int aktk, int n, int m){
    queue<pair<int, int>> kol;
    odw[akti][aktk] = 0;
    kol.push({akti, aktk});

    while (!kol.empty()){
        akti = kol.front().first;
        aktk = kol.front().second;
        kol.pop();

        for (int i = 0; i < 8; i++){
            int ni = akti + ruchy[i].first;
            int nk = aktk + ruchy[i].second;
            if (inRange(ni, nk, n, m) && szach[ni][nk] != 'x' && odw[ni][nk] == -1){
                odw[ni][nk] = odw[akti][aktk] + 1;
                kol.push({ni, nk});
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

    int si, sk;
    int ki, kk;
    for (int i = 0; i < n; i++){
        for (int k = 0; k < m; k++){
            char x;
            cin >> x;
            szach[i][k] = x;
            if (x == 'z'){
                si = i;
                sk = k;
            } else if (x == 'n'){
                ki = i;
                kk = k;
            }
        }
    }

    for (int i = 0; i < n; i++){
        for (int k = 0; k < m; k++){
            odw[i][k] = -1;
        }
    }

    bfs(si, sk, n, m);

    if (odw[ki][kk] == -1){
        cout << "NIE" << endl;
    } else {
        cout << odw[ki][kk] << endl;
    }

    return 0;
}

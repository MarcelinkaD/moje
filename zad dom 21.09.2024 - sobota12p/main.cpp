// 1) https://szkopul.edu.pl/problemset/problem/jz2F2uHp8uk_drXEPQExeDl5/site/?key=statement
/*
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAXN = 1000004;
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

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    bfs(1);

    for (int i = 1; i <= n; i++) {
        if (!czy_odw[i]) {
            cout << -1 << ' ';
        } else {
            cout << odl[i] << ' ';
        }
    }

    return 0;
}
*/

// 2) https://cses.fi/problemset/task/1193
/*
#include <iostream>
#include <string>
#include <queue>
#include <vector>
using namespace std;

const int MAXN = 1003;
vector<pair<int, int>> graf[MAXN][MAXN];
string lab[MAXN];
bool czy_odw[MAXN][MAXN];
int ruchy[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

bool inRange(int ny, int nx, int n, int m) {
    return ((ny < n && nx < m) && (0 <= ny && 0 <= nx));
}

vector<pair<int, int>> bfs(int si, int sj, int ki, int kj) {
    queue<vector<pair<int, int>>> kol;
    kol.push({make_pair(si, sj)});
    czy_odw[si][sj] = 1;

    while (!kol.empty()) {
        vector<pair<int, int>> sciezka = kol.front();
        int sciezka_len = sciezka.size();
        pair<int, int> akt_wie = sciezka[sciezka_len - 1];
        kol.pop();
        int akt_i = akt_wie.first, akt_j = akt_wie.second;

        if (akt_i == ki && akt_j == kj) {
            return sciezka;
        }

        for (int i = 0; i < graf[akt_i][akt_j].size(); i++) {
            pair<int, int> sasiad = graf[akt_i][akt_j][i];
            if (!czy_odw[sasiad.first][sasiad.second]) {
                czy_odw[sasiad.first][sasiad.second] = 1;
                vector<pair<int, int>> nowa_scie = sciezka;
                nowa_scie.push_back(sasiad);
                kol.push(nowa_scie);
            }
        }
    }
    return {};
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++){
        string wiersz;
        cin >> wiersz;
        lab[i] = wiersz;
    }

    int si, sj, ki, kj;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (lab[i][j] != '#') {
                for (int k = 0; k < 4; k++) {
                    int ni, nj;
                    ni = i + ruchy[k][0];
                    nj = j + ruchy[k][1];

                    if (inRange(ni, nj, n, m) && lab[ni][nj] != '#') {
                        graf[i][j].push_back(make_pair(ni, nj));
                    }

                }

                if (lab[i][j] == 'A') {
                    si = i, sj = j;
                }

                if (lab[i][j] == 'B') {
                    ki = i, kj = j;
                }
            }
        }
    }

    if (graf[si][sj].size() == 0 || graf[ki][kj].size() == 0) {
        cout << "NO" << endl;
        return 0;
    }

    vector<pair<int, int>> sciezka = bfs(si, sj, ki, kj);

    if (sciezka.size() == 0) {
        cout << "NO" << endl;
    } else {
        cout << "YES" << endl;
        cout << sciezka.size() - 1 << endl;
        pair<int, int> poprzedni = sciezka[0];

        for (int i = 1; i < sciezka.size(); i++) {
            pair<int, int> sasiad = sciezka[i];
            if (poprzedni.first < sasiad.first) {
                cout << 'D';
            } else if (poprzedni.first > sasiad.first) {
                cout << 'U';
            } else if (poprzedni.second < sasiad.second) {
                cout << 'R';
            } else {
                cout << 'L';
            }
            poprzedni = sasiad;
        }
    }

    return 0;
}
*/

// 3) https://szkopul.edu.pl/problemset/problem/CfSEK4ACOcAPaAfX29Fp7Tud/site/?key=statement
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXN = 9;
vector<int> graf[MAXN];
int czy_odw[MAXN];
int wyspy[MAXN];

void dfs(int akt_v, int akt_znacznik, int akt_oznaczenie) {
    czy_odw[akt_v] = akt_oznaczenie;
    wyspy[akt_v] = akt_znacznik;
    for (int i = 0; i < graf[akt_v].size(); i++) {
        int sasiad = graf[akt_v][i];
        if (czy_odw[sasiad] != akt_oznaczenie) {
            dfs(sasiad, akt_znacznik, akt_oznaczenie);
        }
    }
}

int bfs(int pocz, int kon, int akt_oznaczenie) {
    queue<vector<int>> kol;
    kol.push({pocz});
    czy_odw[pocz] = akt_oznaczenie;

    while (!kol.empty()) {
        vector<int> sciezka = kol.front();
        int sciezka_len = sciezka.size();
        int akt_wie = sciezka[sciezka_len - 1];
        kol.pop();

        if (akt_wie == kon) {
            return sciezka.size() - 1;
        }

        for (int i = 0; i < graf[akt_wie].size(); i++) {
            int sasiad = graf[akt_wie][i];
            if (czy_odw[sasiad] != akt_oznaczenie) {
                czy_odw[sasiad] = akt_oznaczenie;
                vector<int> nowa_scie = sciezka;
                nowa_scie.push_back(sasiad);
                kol.push(nowa_scie);
            }
        }
    }
    return 0;
}

int main() {
    int n, m, q, akt_znacznik = 1, akt_oznaczenie = 1;
    cin >> n >> m >> q;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {
        if (czy_odw[i] != akt_oznaczenie) {
            dfs(i, akt_znacznik, akt_oznaczenie);
            akt_znacznik++;
        }
    }

    akt_oznaczenie = 2;
    for (int k = 0; k < q; k++) {
        int pocz, kon, d;
        cin >> pocz >> kon >> d;

        if (wyspy[pocz] != wyspy[kon]) {
            cout << "NIE" << endl;
        } else {
            int dlugosc_sciezki = bfs(pocz, kon, akt_oznaczenie);
            if (dlugosc_sciezki == d) {
                cout << "TAK" << endl;
            } else {
                cout << "NIE" << endl;
            }
        }
        akt_oznaczenie++;
    }

    return 0;
}


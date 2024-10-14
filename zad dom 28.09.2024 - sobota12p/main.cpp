// 1) https://szkopul.edu.pl/problemset/problem/CfSEK4ACOcAPaAfX29Fp7Tud/site/?key=statement
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXN = 5004;
vector<int> graf[MAXN];
pair<int, int> odl[MAXN];
pair<int, int> czy_odw[MAXN];

void bfs(int od, int jaki_znacznik) {
    queue<pair<int, bool>> kol;
    odl[od].second = 0;
    kol.push(make_pair(od, 1));

    while (!kol.empty()) {
        pair<int, bool> u = kol.front();
        int wie = u.first;
        bool czy_parz = u.second;
        kol.pop();

        for (int i = 0; i < graf[wie].size(); i++){
            int sasiad = graf[wie][i];
            if (czy_parz) {
                if (czy_odw[sasiad].first != jaki_znacznik){
                    czy_odw[sasiad].first = jaki_znacznik;
                    odl[sasiad].first = odl[wie].second + 1;
                    kol.push(make_pair(sasiad, 0));
                }
            } else {
                if (czy_odw[sasiad].second != jaki_znacznik){
                    czy_odw[sasiad].second = jaki_znacznik;
                    odl[sasiad].second = odl[wie].first + 1;
                    kol.push(make_pair(sasiad, 1));
                }
            }
        }

    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m, k, znacznik = 1;
    cin >> n >> m >> k;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    for (int i = 0; i < k; i++){
        int pocz, kon, d;
        cin >> pocz >> kon >> d;
        bfs(pocz, znacznik);

        int odl_parz = odl[kon].second;
        int odl_nieparz = odl[kon].first;

        if (d % 2 == 0) {
            if (czy_odw[kon].second != znacznik) {
                cout << "NIE" << endl;
            } else {
                if (d < odl_parz) {
                    cout << "NIE" << endl;
                } else {
                    cout << "TAK" << endl;
                }
            }
        } else {
            if (czy_odw[kon].first != znacznik) {
                cout << "NIE" << endl;
            } else {
                if (d < odl_nieparz) {
                    cout << "NIE" << endl;
                } else {
                    cout << "TAK" << endl;
                }
            }
        }
        znacznik++;
    }

    return 0;
}

// 2) Las (str. 135)
/*
#include <iostream>
#include <queue>
using namespace std;

int n, d, min_licz = 1000000009, max_licz = -1000000009;
const int MAXN = 1005;
int las[MAXN][MAXN];
int czy_odw[MAXN][MAXN];
int ruchy[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

bool inRange(int ny, int nx, int n) {
    return ((ny < n && nx < n) && (0 <= ny && 0 <= nx));
}

int bfs(int pi, int pj, int max_liczba) {
    int wyn = 0;
    queue<pair<int, int>> kol;
    kol.push(make_pair(pi, pj));
    czy_odw[pi][pj] = max_liczba;

    while (!kol.empty()) {
        int i = kol.front().first, j = kol.front().second;
        wyn++;
        kol.pop();

        for (int k = 0; k < 4; k++){
            int ni = i + ruchy[k][0];
            int nj = j + ruchy[k][1];

            if (inRange(ni, nj, n)) {
                if (las[ni][nj] <= max_liczba && czy_odw[ni][nj] != max_liczba) {
                    kol.push(make_pair(ni, nj));
                    czy_odw[ni][nj] = max_liczba;
                }
            }
        }
    }

    return wyn;
}

bool czy_sie_da(int co_szukamy){
    int ile_mamy = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (czy_odw[i][j] != co_szukamy && las[i][j] <= co_szukamy) {
                ile_mamy = max(ile_mamy, bfs(i, j, co_szukamy));
            }
        }
    }
    return ile_mamy >= d;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> d;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> las[i][j];
            min_licz = min(min_licz, las[i][j]);
            max_licz = max(max_licz, las[i][j]);
        }
    }

    while (min_licz != max_licz) {
        int srodek = (min_licz + max_licz) / 2;
        if (czy_sie_da(srodek)) {
            max_licz = srodek;
        } else {
            min_licz = srodek + 1;
        }
    }

    cout << min_licz << endl;

    return 0;
}
*/

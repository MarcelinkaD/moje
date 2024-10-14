// 1) https://szkopul.edu.pl/problemset/problem/CfSEK4ACOcAPaAfX29Fp7Tud/site/?key=statement

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct zap {
    int kon;
    int odl;
    int num;
};

const int MAXN = 5004;
const int MAXK = 1000004;
vector<int> graf[MAXN];
pair<int, int> odl[MAXN];
pair<int, int> czy_odw[MAXN];
vector<zap> zapytania[MAXK];
bool wyn[MAXK];

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

    int n, m, k, znacznik = 1, max_pocz = -1;
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
        max_pocz = max(max_pocz, pocz);
        zapytania[pocz].push_back({kon, d, i});
    }

    for (int i = 1; i <= max_pocz; i++){
        if (zapytania[i].size() > 0){
            bfs(i, znacznik);
            for (int j = 0; j < zapytania[i].size(); j++){
                int kon = zapytania[i][j].kon;
                int index = zapytania[i][j].num;
                int d = zapytania[i][j].odl;
                int odl_parz = odl[kon].second;
                int odl_nieparz = odl[kon].first;

                if (d % 2 == 0) {
                    if (czy_odw[kon].second != znacznik) {
                        wyn[index] = 0;
                    } else {
                        if (d < odl_parz) {
                            wyn[index] = 0;
                        } else {
                            wyn[index] = 1;
                        }
                    }
                } else {
                    if (czy_odw[kon].first != znacznik) {
                        wyn[index] = 0;
                    } else {
                        if (d < odl_nieparz) {
                            wyn[index] = 0;
                        } else {
                            wyn[index] = 1;
                        }
                    }
                }
            }
        znacznik++;
        }

    }

    for (int i = 0; i < k; i++) {
        if (wyn[i]) {
            cout << "TAK" << endl;
        } else {
            cout << "NIE" << endl;
        }
    }

    return 0;
}


// 2) https://app.codility.com/programmers/task/odd_network/
/*
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXN = 500004;
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

int solution(vector<int> &A, vector<int> &B)
{
    int n = A.size();
    int max_licz = -1;
    int w = 0;
    int znacznik = 1;

    for (int i = 0; i < n; i++) {
        graf[A[i]].push_back(B[i]);
        graf[B[i]].push_back(A[i]);
        max_licz = max(max(A[i], B[i]), max_licz);
    }

    for (int i = 0; i <= max_licz; i++){
        if (graf[i].size() > 0){
            bfs(i, znacznik);
            for (int k = 0; k <= max_licz; k++){
                if (czy_odw[k].first == znacznik) {
                    w++;
                }
            }
        znacznik++;
        }
    }
    return w / 2;

}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    //vector<int> A = {0, 3, 4, 2, 6, 3};
    //vector<int> B = {3, 1, 3, 3, 3, 5};

    //vector<int> A = {0, 4, 4, 2, 7, 6, 3};
    //vector<int> B = {3, 5, 1, 3, 4, 3, 4};

    vector<int> A = {0, 4, 2, 2, 4};
    vector<int> B = {1, 3, 1, 3, 5};

    cout << solution(A, B) << endl;

    return 0;
}

*/

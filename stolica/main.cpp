//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/sto/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000005;
vector<int> graf[MAXN];
vector<int> graftra[MAXN];
int ktora_grupa[MAXN];
int sss[MAXN];
stack<int> stos;
vector<int> wynik;
vector<int> sss_elementy[MAXN];

void DFS(int v, int akt_zna){
    ktora_grupa[v] = akt_zna;
    for (int i = 0; i < graf[v].size(); i++) {
        int sasiad = graf[v][i];
        if (ktora_grupa[sasiad] == 0) {
            DFS(sasiad, akt_zna);
        }
    }
    stos.push(v);
}

void DFS2(int v, int akt_zna){
    sss[v] = akt_zna;
    sss_elementy[akt_zna].push_back(v);
    for (int i = 0; i < graftra[v].size(); i++) {
        int sasiadT = graftra[v][i];
        if (ktora_grupa[v] == ktora_grupa[sasiadT] && sss[sasiadT] == 0) {
            DFS2(sasiadT, akt_zna);
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
        graftra[b].push_back(a);
    }

    if (n == 1){
        cout << 1 << endl;
        cout << 1 << endl;
    }

    for (int i = 1; i <= n; i++){
        if (ktora_grupa[i] == 0){
            DFS(i, i);
        }
    }

    int akt_zna = 1;
    while (!stos.empty()) {
        int u = stos.top();
        stos.pop();
        if (sss[u] == 0) {
            DFS2(u, akt_zna);
            akt_zna++;
        }
    }

    if (akt_zna == 2) {
        cout << n << endl;
        for (int i = 1; i <= n; i++){
            cout << i << ' ';
        }
        return 0;
    }

    vector<unordered_set<int>> wychodzace_sss(n + 1);
    vector<unordered_set<int>> wchodzace_sss(n + 1);
    vector<pair<int, int>> wchadzace_i_wychodzace(n + 1, {0, 0});
    for (int i = 1; i <= n; i++){
        for (int sasiad : graf[i]){
            if (sss[i] != sss[sasiad]){
                wychodzace_sss[sss[i]].insert(sss[sasiad]);
                wchodzace_sss[sss[sasiad]].insert(sss[i]);
            }
        }
    }

    for (int i = 1; i < akt_zna; i++) {
        wchadzace_i_wychodzace[i].first = wchodzace_sss[i].size();
        wchadzace_i_wychodzace[i].second = wychodzace_sss[i].size();

        if (wchadzace_i_wychodzace[i].first == 0 && wchadzace_i_wychodzace[i].second != 0){
            if (wynik.size() != 0) {
                cout << "KLOPS" << endl;
                return 0;
            }
            for (const auto &j : sss_elementy[i]){
                wynik.push_back(j);
            }
        } else if (wchadzace_i_wychodzace[i].first == 0 && wchadzace_i_wychodzace[i].second == 0) {
            cout << "KLOPS" << endl;
            return 0;
        }

    }

    if (wynik.size() == 0) {
        cout << "KLOPS" << endl;
        return 0;
    }

    cout << wynik.size() << endl;
    for (const auto &i : wynik) {
        cout << i << ' ';
    }

    return 0;
}

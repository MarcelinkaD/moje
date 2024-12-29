//https://sio2.mimuw.edu.pl/c/oi32-1/p/bit/
#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int MAXN = 3000;
vector<vector<int>> bitada;
vector<vector<int>> bajtogrod;
int rodzice_bitada[MAXN];
int rodzice_bajtogrod[MAXN];
ll wyniki[MAXN][MAXN];
int n, m;
ll k;

void przypisz_rodzicow(int korzen, vector<vector<int>> &drzewo, int rodzic[]) {
    queue<int> kol;
    kol.push(korzen);
    rodzic[korzen] = -1;
    while (!kol.empty()) {
        int u = kol.front();
        kol.pop();
        for (int i = 0; i < drzewo[u].size(); i++) {
            int sasiad = drzewo[u][i];
            if (sasiad != rodzic[u]) {
                rodzic[sasiad] = u;
                kol.push(sasiad);
            }
        }
    }
}

ll na_ile_sposobow(int u, int v) {
    if(wyniki[u][v] != -1)
        return wyniki[u][v];

    vector<int> dzieci_u;
    for (auto &dziecko: bitada[u]){
        if (dziecko != rodzice_bitada[u]){
            dzieci_u.push_back(dziecko);
        }
    }

    vector<int> dzieci_v;
    for (auto &dziecko : bajtogrod[v]){
        if (dziecko != rodzice_bajtogrod[v]){
            dzieci_v.push_back(dziecko);
        }
    }

    if (dzieci_u.size() > dzieci_v.size()){
        wyniki[u][v] = 0;
        return wyniki[u][v];
    }

    if (dzieci_u.empty()){
        wyniki[u][v] = 1;
        return wyniki[u][v];
    }

    ll wynik = 0;
    if (dzieci_u.size() == 1){
        for (int i = 0; i < dzieci_v.size(); i++){
            int dziecko_v = dzieci_v[i];
            ll liczba_sposobow = na_ile_sposobow(dzieci_u[0], dziecko_v);
            wynik = (wynik + liczba_sposobow) % k;
        }
    }
    else if (dzieci_u.size() == 2){
        for (int i = 0; i < dzieci_v.size(); ++i){
            for (int j = 0; j < dzieci_v.size(); ++j){
                if (j == i) {
                    continue;
                }
                int dziecko_v1 = dzieci_v[i];
                int dziecko_v2 = dzieci_v[j];
                ll liczba_sposobow1 = na_ile_sposobow(dzieci_u[0], dziecko_v1);
                ll liczba_sposobow2 = na_ile_sposobow(dzieci_u[1], dziecko_v2);
                wynik = (wynik + (liczba_sposobow1 * liczba_sposobow2) % k) % k;
            }
        }
    }
    else if (dzieci_u.size() == 3){
        for (int i = 0; i < dzieci_v.size(); ++i){
            for (int j = 0; j < dzieci_v.size(); ++j){
                if (j == i) {
                    continue;
                }
                for (int l = 0; l < dzieci_v.size(); ++l){
                    if (l == i || l == j) {
                        continue;
                    }
                    int dziecko_v1 = dzieci_v[i];
                    int dziecko_v2 = dzieci_v[j];
                    int dziecko_v3 = dzieci_v[l];
                    ll liczba_sposobow1 = na_ile_sposobow(dzieci_u[0], dziecko_v1);
                    ll liczba_sposobow2 = na_ile_sposobow(dzieci_u[1], dziecko_v2);
                    ll liczba_sposobow3 = na_ile_sposobow(dzieci_u[2], dziecko_v3);
                    wynik = (wynik + ((liczba_sposobow1 * liczba_sposobow2) % k * liczba_sposobow3) % k) % k;
                }
            }
        }
    }

    wyniki[u][v] = wynik;
    return wyniki[u][v];
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m >> k;

    bitada.assign(n + 1, vector<int>());
    bajtogrod.assign(m + 1, vector<int>());

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        bitada[a].push_back(b);
        bitada[b].push_back(a);
    }

    for (int i = 0; i < m - 1; i++) {
        int a, b;
        cin >> a >> b;
        bajtogrod[a].push_back(b);
        bajtogrod[b].push_back(a);
    }

    przypisz_rodzicow(1, bitada, rodzice_bitada);
    ll wyn = 0;
    for (int akt_korzen = 1; akt_korzen <= m; akt_korzen++){
        przypisz_rodzicow(akt_korzen, bajtogrod, rodzice_bajtogrod);

        for (int u = 1; u <= n; ++u){
            for (int v = 1; v <= m; ++v){
                wyniki[u][v] = -1;
            }
        }

        ll liczba_sposobow = na_ile_sposobow(1, akt_korzen);
        wyn = (wyn + liczba_sposobow) % k;
    }

    cout << wyn;
    return 0;
}


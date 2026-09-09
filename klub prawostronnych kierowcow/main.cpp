#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
bool graf[MAXN][MAXN];
bool czy_odw[MAXN][MAXN][4];
pair<int,int> rodzic_pol[MAXN][MAXN][4];
int kier_rodz[MAXN][MAXN][4];
queue<pair<pair<int, int>, int>> kol;
vector<pair<int, int>> ruchy = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

int wyz_kier(int i, int j, int ni, int nj){
    if (ni < i){
        return 0; // z dolu
    }
    if (nj > j){
        return 1; // z lewej
    }
    if (ni > i){
        return 2; // z gory
    }
    if (nj < j){
        return 3; // z prawej
    }
    return -1;
}


bool czy_git(int ni, int nj, int i, int j, int n, int m, int kier, int nkier){
    if ((ni >= n || nj >= m) || (ni < 0 || nj < 0)){
        return false;
    }
    if (graf[ni][nj] == 1) {
        return false;
    }
    if (kier != -1 && ((kier + 3) % 4 == nkier || (kier + 2) % 4 == nkier)){
        return false;
    }
    return true;
}

vector<pair<int,int>> wyz_scie(int ki, int kj, int ost_kier, int pi, int pj){
    vector<pair<int,int>> scie;
    int a = ki;
    int b = kj;
    int k = ost_kier;
    while (true){
        scie.push_back({a, b});
        if (a == pi && b == pj) {
            break;
        }
        pair<int,int> p = rodzic_pol[a][b][k];
        int pk = kier_rodz[a][b][k];
        a = p.first;
        b = p.second;
        k = pk;
    }
    reverse(scie.begin(), scie.end());
    return scie;
}

vector<pair<int, int>> znajdz(int pi, int pj, int ki, int kj, int n, int m) {
    kol.push({{pi, pj}, -1});
    while (!kol.empty()){
        auto akt = kol.front().first;
        int kier = kol.front().second;
        kol.pop();
        int i = akt.first;
        int j = akt.second;

        for (auto ruch : ruchy){
            int ni = i + ruch.first;
            int nj = j + ruch.second;
            int nkier = wyz_kier(i, j, ni, nj);
            if (nkier == -1) continue;
            if (czy_git(ni, nj, i, j, n, m, kier, nkier) && !czy_odw[ni][nj][nkier]) {
                czy_odw[ni][nj][nkier] = true;
                rodzic_pol[ni][nj][nkier] = {i, j};
                kier_rodz[ni][nj][nkier] = kier;
                if (ni == ki && nj == kj){
                    return wyz_scie(ki, kj, nkier, pi, pj);
                }
                kol.push({{ni, nj}, nkier});
            }
        }
    }
    return {{-1, -1}};
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++){
        string x;
        cin >> x;
        for (int j = 0; j < m; j++){
            graf[i][j] = (bool)(x[j] - '0');
        }
    }

    int pi, pj, ki, kj;
    cin >> pi >> pj >> ki >> kj;

    if (graf[pi - 1][pj - 1] == 1 || graf[ki - 1][kj - 1] == 1){
        cout << "NIE" << '\n';
        return 0;
    }

    vector<pair<int,int>> wyn = znajdz(pi - 1, pj - 1, ki - 1, kj - 1, n, m);
    if (wyn[0].first == -1){
        cout << "NIE" << '\n';
        return 0;
    }

    cout << wyn.size() << '\n';
    for (auto p : wyn){
        cout << p.first + 1 << ' ' << p.second + 1 << '\n';
    }
    return 0;
}

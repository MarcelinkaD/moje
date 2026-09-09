#include <bits/stdc++.h>
using namespace std;

vector<string> plansza;
vector<pair<int, int>> ruchy = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
bool odw[105][105][1005];
int n, m;
bool znalazl = false;
unordered_map<char, vector<pair<int, int>>> wsp;

bool czy_git(int i, int j){
    return (i < n && j < m && 0 <= i && 0 <= j);
}

void wyzeruj(int k){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            for (int z = 0; z < k; z++){
                odw[i][j][z] = 0;
            }
        }
    }
}

void dfs(string slowo, string akt_slowo, int i, int j, int akt_lit) {
    odw[i][j][akt_lit] = true;
    if (slowo == akt_slowo) {
        znalazl = true;
        return;
    }
    if (slowo.size() == akt_slowo.size()){
        return;
    }
    for (auto ruch : ruchy){
        pair<int, int> u = {i + ruch.first, j + ruch.second};
        if (czy_git(u.first, u.second) && slowo[akt_lit + 1] == plansza[u.first][u.second] && !odw[u.first][u.second][akt_lit + 1]){
            dfs(slowo, akt_slowo + plansza[u.first][u.second], u.first, u.second, akt_lit + 1);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++){
        string rzad;
        cin >> rzad;
        plansza.push_back(rzad);
        for (int j = 0; j < m; j++){
            wsp[rzad[j]].push_back({i, j});
        }
    }

    int q;
    cin >> q;

    while (q > 0){
        string x;
        cin >> x;
        char pierw = x[0];
        string pocz;
        pocz += pierw;
        for (auto wspolrzedne : wsp[pierw]) {
            dfs(x, pocz, wspolrzedne.first, wspolrzedne.second, 0);
            if (znalazl){
                cout << "TAK" << '\n';
                break;
            }
        }
        if (znalazl == 0){
            cout << "NIE" << '\n';
        }
        znalazl = false;
        wyzeruj(x.size());
        q--;
    }

    return 0;
}

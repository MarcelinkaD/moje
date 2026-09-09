#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> przed;
vector<vector<int>> po;
vector<pair<int, int>> start_pos;
vector<pair<int, int>> akt_pos;
vector<pair<int, int>> kon_pos;
vector<tuple<int, int, int>> wyn;
set<pair<int, int>> kon_pos_zbior;
vector<pair<int, int>> ruchy = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

bool inRange(pair<int, int> pole, int n){
    return pole.first <= n && pole.second <= n && pole.first > 0 && pole.second > 0;
}

bool czy_moze_isc(pair<int, int> pole, int n, int k, int ignoruj){
    if (inRange(pole, n)){
        for (auto ruch : ruchy){
            pair<int, int> n_pole;
            n_pole.first = pole.first + ruch.first;
            n_pole.second = pole.second + ruch.second;
            if (inRange(n_pole, n)){
                for (int i = 1; i <= k; i++){
                    if (i != ignoruj && akt_pos[i] == n_pole){
                        return false;
                    }
                }
            }
        }
        return true;
    }
    return false;
}

bool czy_kon(int k){
    for (int i = 1; i <= k; i++){
        if (akt_pos[i] != kon_pos[i]){
            return false;
        }
    }
    return true;
}

vector<pair<int, int>> bfs(pair<int, int> start_pole, pair<int, int> kon_pole, int n, int k, int ignoruj){
    queue<pair<int, int>> kol;
    unordered_map<int, unordered_map<int, pair<int, int>>> poprzedni;
    kol.push(start_pole);
    poprzedni[start_pole.first][start_pole.second] = {-1, -1};
    
    while (!kol.empty()){
        auto akt_wie = kol.front();
        kol.pop();
        for (auto ruch : ruchy){
            pair<int, int> n_pole;
            n_pole.first = akt_wie.first + ruch.first;
            n_pole.second = akt_wie.second + ruch.second;
            if (czy_moze_isc(n_pole, n, k, ignoruj) && poprzedni[n_pole.first].count(n_pole.second) == 0){
                poprzedni[n_pole.first][n_pole.second] = akt_wie;
                kol.push(n_pole);
            }
        }
    }

    if (poprzedni[kon_pole.first].count(kon_pole.second) == 0){
        return {};
    }
    vector<pair<int, int>> sciezka;
    pair<int, int> akt_wie = kon_pole;

    while (akt_wie != make_pair(-1, -1)) {
        sciezka.push_back(akt_wie);
        akt_wie = poprzedni[akt_wie.first][akt_wie.second];
    }
    reverse(sciezka.begin(), sciezka.end());
    return sciezka;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, k;
    cin >> n >> k;
    przed.resize(n + 1, vector<int>(n + 1));
    po.resize(n + 1, vector<int>(n + 1));
    start_pos.resize(k + 1);
    akt_pos.resize(k + 1);
    kon_pos.resize(k + 1);

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            cin >> przed[i][j];
            if (przed[i][j] != 0){
                start_pos[przed[i][j]] = {i, j};
                akt_pos[przed[i][j]] = {i, j};
            }
        }
    }

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            cin >> po[i][j];
            if (po[i][j] != 0){
                kon_pos[po[i][j]] = {i, j};
                kon_pos_zbior.insert({i, j});
            }
        }
    }

    bool czy_git = czy_kon(k);
    if (czy_git){
        cout << "TAK" << '\n';
        cout << 0 << '\n';
        return 0;
    }

    czy_git = false;
    for (int i = 1; i <= k; i++){
        pair<int, int> akt_pole = start_pos[i];
        for (auto ruch : ruchy){
            pair<int, int> n_pole;
            n_pole.first = akt_pole.first + ruch.first;
            n_pole.second = akt_pole.second + ruch.second;
            if (czy_moze_isc(n_pole, n, k, i)){
                czy_git = true;
                break;
            }
        }
    }

    if (czy_git == false){
        cout << "NIE" << '\n';
        return 0;
    }

    unordered_map<int, unordered_map<int, int>> zajete_pola;
    for (int krol = 1; krol <= k; krol++){
        int i = akt_pos[k].first;
        int j = akt_pos[k].second;
        zajete_pola[i][j] = krol;
    }

    while (!czy_kon(k)){
        vector<int> do_prze;
        for (int krol = 1; krol <= k; krol++){
            if (akt_pos[krol] == kon_pos[krol]){
                continue;
            }
            pair<int, int> kon_pole = kon_pos[krol];
            if (zajete_pola[kon_pole.first].count(kon_pole.second) == 0){
                do_prze.push_back(krol);
            }
        }

        int akt_krol = -1;
        pair<int, int> kon;
        vector<pair<int, int>> sciezka;

        for (int krol : do_prze){
            pair<int, int> kon_pole = kon_pos[krol];
            sciezka = bfs(akt_pos[krol], kon_pole, n, k, krol);
            if (!sciezka.empty()){
                akt_krol = krol;
                kon = kon_pos[akt_krol];
                break;
            }
        }

        if (akt_krol == -1){
            for (int krol = 1; krol <= k; krol++){
                if (akt_pos[krol] != kon_pos[krol]){
                    akt_krol = krol;
                    break;
                }
            }
            bool czy_git = false;
            for (int i = 1; i <= n; i++){
                for (int j = 1; j <= n; j++){
                    pair<int, int> akt_pole = {i, j};
                    if (zajete_pola[i].count(j) == 0 && kon_pos_zbior.count(akt_pole) == 0 && 
                        czy_moze_isc(akt_pole, n, k, akt_krol)){
                        sciezka = bfs(akt_pos[akt_krol], akt_pole, n, k, akt_krol);
                        if (!sciezka.empty()){
                            kon = akt_pole;
                            czy_git = true;
                            break;
                        }
                    }
                }
            }
            if (!czy_git){
                cout << "NIE" << '\n';
                return 0;
            }
        }

        if (sciezka.size() == 0){
            cout << "NIE" << '\n';
            return 0;
        }

        for (int i = 1; i < sciezka.size(); i++){
            pair<int, int> pole = sciezka[i];
            auto akt_pole = akt_pos[akt_krol];
            zajete_pola[akt_pole.first].erase(akt_pole.second);
            akt_pos[akt_krol] = pole;
            zajete_pola[pole.first][pole.second] = akt_krol;
            wyn.emplace_back(akt_krol, pole.first, pole.second);
        }
    }

    cout << "TAK" << '\n';
    cout << wyn.size() << '\n';
    for (int i = 0; i < wyn.size(); i++){
        int a = get<0>(wyn[i]);
        int b = get<1>(wyn[i]);
        int c = get<2>(wyn[i]);
        cout << a << ' ' << b << ' ' << c << '\n';
    }

    return 0;
}
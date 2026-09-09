#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

struct pole{
    int wie;
    int kol;
};

vector<string> plansza;
vector<vector<int>> odl;
vector<ll> drzewo;
vector<ll> przep;
vector<vector<bool>> czy_fort;
vector<int> ile_fort_odl;

void stworz(int akt_wierz, int start_odp, int kon_odp){
    if (start_odp == kon_odp){
        drzewo[akt_wierz] = (ll)start_odp - 1;
        return;
    }
    int srodek = (start_odp + kon_odp) / 2;
    stworz(akt_wierz * 2, start_odp, srodek);
    stworz(akt_wierz * 2 + 1, srodek + 1, kon_odp);
    drzewo[akt_wierz] = max(drzewo[akt_wierz * 2], drzewo[akt_wierz * 2 + 1]);
}

void przepchnij(int akt_wie, int pocz_odp, int kon_odp){
    if (przep[akt_wie] != 0){
        drzewo[akt_wie] += przep[akt_wie];
        if (pocz_odp != kon_odp){
            przep[akt_wie * 2] += przep[akt_wie];
            przep[akt_wie * 2 + 1] += przep[akt_wie];
        }
        przep[akt_wie] = 0;
    }
}

void zmien(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt, ll war){
    przepchnij(akt_wie, pocz_odp, kon_odp);
    if (pocz_odp > kon_odp || pocz_odp > kon_pyt || kon_odp < pocz_pyt){
        return;
    }
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        przep[akt_wie] += war;
        przepchnij(akt_wie, pocz_odp, kon_odp);
        return;
    }
    int l = akt_wie * 2;
    int p = akt_wie * 2 + 1;
    int srodek = (pocz_odp + kon_odp) / 2;
    zmien(l, pocz_odp, srodek, pocz_pyt, kon_pyt, war);
    zmien(p, srodek + 1, kon_odp, pocz_pyt, kon_pyt, war);
    drzewo[akt_wie] = max(drzewo[l], drzewo[p]);
}

ll odp(int akt_wie, int pocz_odp, int kon_odp, int pocz_pyt, int kon_pyt){
    przepchnij(akt_wie, pocz_odp, kon_odp);
    if (pocz_odp > kon_odp || pocz_odp > kon_pyt || kon_odp < pocz_pyt){
        return LLONG_MIN;
    }
    if (pocz_pyt <= pocz_odp && kon_odp <= kon_pyt){
        return drzewo[akt_wie];
    }
    int l = akt_wie * 2;
    int p = akt_wie * 2 + 1;
    int srodek = (pocz_odp + kon_odp) / 2;
    return max(odp(l, pocz_odp, srodek, pocz_pyt, kon_pyt),
    odp(p, srodek + 1, kon_odp, pocz_pyt, kon_pyt));
}

bool inRange(pole x, int n){
    return x.wie <= n && x.kol <= n && x.wie > 0 && x.kol > 0;
}

int bfs(int n){
    queue<pole> kol;
    pole start;
    start.wie = 1;
    start.kol = 1;
    kol.push(start);
    odl[start.wie][start.kol] = 0;
    
    int max_odl = 0;
    vector<pair<int, int>> ruchy = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    while (!kol.empty()){
        pole akt_wie = kol.front();
        kol.pop();
        
        for (auto ruch : ruchy){
            pole n_pole;
            n_pole.kol = akt_wie.kol + ruch.first;
            n_pole.wie = akt_wie.wie + ruch.second;
            if (inRange(n_pole, n) && odl[n_pole.wie][n_pole.kol] == -1 && plansza[n_pole.wie][n_pole.kol] != '#'){
                odl[n_pole.wie][n_pole.kol] = odl[akt_wie.wie][akt_wie.kol] + 1;
                max_odl = max(max_odl, odl[n_pole.wie][n_pole.kol]);
                kol.push(n_pole);
            }
        }
    }
    return max_odl;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;
    plansza.resize(n + 1);
    odl.resize(n + 1, vector<int>(n + 1, -1));
    czy_fort.resize(n + 1, vector<bool>(n + 1, false));

    for (int i = 1; i <= n; i++){
        string x;
        cin >> x;
        x = '#' + x;
        plansza[i] = x;
    }

    int max_odl = bfs(n);
    ile_fort_odl.resize(max_odl + 1, 0);
    drzewo.resize(4 * (max_odl + 1));
    przep.resize(4 * (max_odl + 1));

    stworz(1, 0, max_odl);
    int akt_max_odl = -1;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            if (plansza[i][j] == 'F'){
                czy_fort[i][j] = true;
                int odl_fort = odl[i][j];
                zmien(1, 0, max_odl, 0, odl_fort, (ll)1);
                ile_fort_odl[odl_fort]++;
                akt_max_odl = max(akt_max_odl, odl_fort);
            }
        }
    }

    ll wyn;
    if (akt_max_odl >= 0){
        wyn = odp(1, 0, max_odl, 0, akt_max_odl);
    } else {
        wyn = (ll)0;
    }

    cout << wyn << '\n';
    while (q--){
        int wie, kol;
        cin >> wie >> kol;
        int fort_odl = odl[wie][kol];
        if (czy_fort[wie][kol]){
            zmien(1, 0, max_odl, 0, fort_odl, (ll)-1);
            ile_fort_odl[fort_odl]--;
            if (ile_fort_odl[fort_odl] == 0 && fort_odl == akt_max_odl){
                while (akt_max_odl >= 0 && ile_fort_odl[akt_max_odl] == 0){
                    akt_max_odl--;
                }
            }
            czy_fort[wie][kol] = false;
        } else {
            zmien(1, 0, max_odl, 0, fort_odl, (ll)1);
            ile_fort_odl[fort_odl]++;
            akt_max_odl = max(akt_max_odl, fort_odl);
            czy_fort[wie][kol] = true;
        }
        if (akt_max_odl >= 0){
           wyn = odp(1, 0, max_odl, 0, akt_max_odl);
        } else {
            wyn = 0;
        }
        cout << wyn << '\n';
    }

    return 0;
}
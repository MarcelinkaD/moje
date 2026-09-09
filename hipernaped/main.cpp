#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int B = 60;
vector<vector<int>> f; // f[licz_gal][licz_tun]
vector<vector<int>> jp[B]; // jp[B][licz_gal][licz_tun]
vector<int> czyja;

int gdzie_wyladuje(int akt_wie, ll skok, int ktory_tun) {
    for (int j = 0; j < B; j++){
        if (skok & (1LL << j)){
            akt_wie = jp[j][akt_wie][ktory_tun];
        }
    }
    return akt_wie;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int licz_gal, licz_tun;
    ll ile_skok;
    cin >> licz_gal >> licz_tun >> ile_skok;
    f.resize(licz_gal + 1);
    czyja.resize(licz_gal + 1);

    for (int i = 1; i <= licz_gal; i++){
        f[i].resize(licz_tun + 1);
    }

    for (int i = 0; i < B; i++){
        jp[i].resize(licz_gal + 1);
        for (int k = 1; k <= licz_gal; k++){
            jp[i][k].resize(licz_tun + 1);
        }
    }

    for (int i = 1; i <= licz_gal; i++){
        cin >> czyja[i];
    }

    for (int i = 1; i <= licz_gal; i++){
        for (int k = 1; k <= licz_tun; k++){
            cin >> f[i][k];
        }
    }

    for (int i = 1; i <= licz_gal; i++){
        for (int k = 1; k <= licz_tun; k++){
            jp[0][i][k] = f[i][k];
        }
    }

    for (int j = 1; j < B; j++){
        for (int i = 1; i <= licz_gal; i++){
            for (int k = 1; k <= licz_tun; k++){
                jp[j][i][k] = jp[j - 1][jp[j - 1][i][k]][k];
            }
        }
    }

    int akt_wierz = 1;
    for (int i = 0; i < ile_skok; i++){
        int ktory;
        ll skoki;
        cin >> ktory >> skoki;
        akt_wierz = gdzie_wyladuje(akt_wierz, skoki, ktory);
    }

    cout << czyja[akt_wierz] << endl;

    return 0;
}

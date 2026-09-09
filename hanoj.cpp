#include <bits/stdc++.h>
using namespace std;

struct stos{
    int kon;
    int gdzie;
};

vector<vector<int>> stosy;
vector<int> gdzie_klocek;
stos min_stos1, min_stos2;

int gdzie_sie_da(int akt_stos){
    int wierzch = stosy[akt_stos][0];
    int najm_kon = INT_MAX;
    int gdzie = -1;
    
    if (min_stos1.gdzie != akt_stos && min_stos1.gdzie != -1){
        najm_kon = min_stos1.kon;
        gdzie = min_stos1.gdzie;
    } else if (min_stos2.gdzie != akt_stos && min_stos2.gdzie != -1){
        najm_kon = min_stos2.kon;
        gdzie = min_stos2.gdzie;
    }

    if (wierzch > najm_kon){
        return gdzie;
    }
    return -1;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    stosy.resize(m + 1);
    gdzie_klocek.resize(n + 1);
    min_stos1.kon = INT_MAX;
    min_stos2.kon = INT_MAX;
    min_stos1.gdzie = -1;
    min_stos2.gdzie = -1;

    int gdzie_pust = -1;
    for (int i = 1; i <= m; i++){
        int k;
        cin >> k;
        if (k == 0) {
            gdzie_pust = i;
            continue;
        }
        for (int j = 0; j < k; j++){
            int x;
            cin >> x;
            stosy[i].push_back(x);
            gdzie_klocek[x] = i;
        }
        if (min_stos1.kon > stosy[i].back()){
            min_stos2.kon = min_stos1.kon;
            min_stos2.gdzie = min_stos1.gdzie;
            min_stos1.kon = stosy[i].back();
            min_stos1.gdzie = i;
        } else if (min_stos2.kon > stosy[i].back()){
            min_stos2.kon = stosy[i].back();
            min_stos2.gdzie = i;
        }
    }
    
    int min_wyn = INT_MAX;
    if (gdzie_pust != -1){
        min_wyn = n;
    }
    
    int start_stos = -1;
    int ile_zostaje = 0;
    bool czy_git = true;
    int gdzie_jed = gdzie_klocek[1];
    for (int j = 1; j < (int)stosy[gdzie_jed].size(); j++){
        if (stosy[gdzie_jed][j] != stosy[gdzie_jed][j - 1] + 1){
            czy_git = false;
            break;
        }
    }
    if (czy_git){
        ile_zostaje = (int)stosy[gdzie_jed].size();
        if (min_wyn > n - ile_zostaje){
            min_wyn = n - ile_zostaje;
            start_stos = gdzie_jed;
        }
    } else {
        if (gdzie_pust != -1){
            min_wyn = n;
            start_stos = gdzie_pust;
        } else {
            int dokad_dac = -1;
            for (int akt_stos = 1; akt_stos <= m; akt_stos++){
                if (akt_stos != gdzie_jed){
                    int gdzie = gdzie_sie_da(akt_stos);
                    if (gdzie != -1) {
                        int akt_koszt = (int)stosy[akt_stos].size();
                        if (min_wyn > akt_koszt + n){
                            min_wyn = akt_koszt + n;
                            start_stos = akt_stos;
                            dokad_dac = gdzie;
                        }
                    }
                }
            }
            if (start_stos == -1){
                cout << -1 << '\n';
                return 0;
            }
            cout << min_wyn << '\n';
            for (auto kam : stosy[start_stos]){
                cout << start_stos << ' ' << dokad_dac << '\n';
                gdzie_klocek[kam] = dokad_dac; 
            }
            for (int i = 1; i <= n; i++){
                cout << gdzie_klocek[i] << ' ' << start_stos << '\n';
            }
            return 0;
        }
    }

    if (start_stos == -1){
        cout << -1 << '\n';
        return 0;
    }

    cout << min_wyn << '\n';
    for (int i = ile_zostaje + 1; i <= n; i++){
        cout << gdzie_klocek[i] << ' ' << start_stos << '\n';
    }

    return 0;
}
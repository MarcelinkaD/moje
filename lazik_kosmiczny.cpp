#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
bool SIDO[MAXN];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    int nwd = __gcd(n, m);
    if (nwd == 1 || nwd == 2){
        cout << 2 << '\n';
        cout << "DL" << '\n';
        return 0;
    }
    int ile_w_dol = -1;

    vector<int> dziel_pie_n;
    vector<int> dziel_pie_m;

    int x = n;
    for (int i = 2; i * i <= x; i++){
    if (x % i == 0){
        dziel_pie_n.push_back(i);
        while (x % i == 0){
            x /= i;
        }
    }
    }
    if (x > 1){
        dziel_pie_n.push_back(x);
    }

    x = m;
    for (int i = 2; i * i <= x; i++){
    if (x % i == 0){
        dziel_pie_m.push_back(i);
        while (x % i == 0){
            x /= i;
        }
    }
    }
    if (x > 1){
        dziel_pie_m.push_back(x);
    }

    while (nwd <= max(n, m)){
        for (auto i : dziel_pie_n){
            if (i > 1){
                for (int k = i; k < nwd; k += i){
                    SIDO[k] = 1;
                }
            }
        }

        for (auto i : dziel_pie_m){
            if (i > 1){
                int r = nwd % i;
                if (r == 0){
                    for (int k = i; k < nwd; k += i){
                        SIDO[k] = 1;
                    }
                } else {
                    for (int k = r; k < nwd; k += i){
                        SIDO[k] = 1;
                    }
                }
                
            }
        }

        ile_w_dol = -1;
        for (int i = 1; i < nwd; i++) {
            if (!SIDO[i]){
                ile_w_dol = i;
                break;
            }
        }
        if (ile_w_dol != -1){
            break;
        }
        
        for (int i = 0; i < MAXN; i++){
            SIDO[i] = false;
        }

        nwd++;
    }

    cout << nwd << '\n';
    for (int i = 0; i < ile_w_dol; i++){
        cout << 'D';
    }

    for (int i = 0; i < nwd - ile_w_dol; i++){
        cout << 'L';
    }

    return 0;

}
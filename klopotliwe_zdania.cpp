#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    vector<int> t(n);

    for (int i = 0; i < n; i++){
        cin >> t[i];
    }

    sort(t.begin(), t.end());
    
    ll w = 0;
    for (int i = 0; i < n - 2; i++){
        int pocz = i + 1;
        int kon = n - 1;
        ll szukamy = k - t[i];
        while (pocz < kon){
            if (t[pocz] + t[kon] < szukamy){
                pocz++;
            } else if (t[pocz] + t[kon] > szukamy){
                kon--;
            } else {
                if (t[pocz] == t[kon]){
                    ll ile_pow = kon - pocz + 1;
                    w += ile_pow * (ile_pow - 1) / 2;
                    break;
                } else {
                    ll ile_git_pocz = 1;
                    ll ile_git_kon = 1;
                    while (pocz < kon - 1 && t[pocz + 1] == t[pocz]){
                        ile_git_pocz++;
                        pocz++;
                    }
                    while (kon > pocz + 1 && t[kon - 1] == t[kon]){
                        ile_git_kon++;
                        kon--;
                    }
                    w += ile_git_pocz * ile_git_kon;
                    pocz++;
                    kon--;
                }
            }
        }
    }
    cout << w << '\n';

    return 0;
}
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;

    vector<char> tab;
    tab.resize(n);

    for (int i = 0; i < n; i++){
        char x;
        cin >> tab[i];
    }

    for (int i = 0; i < q; i++){
        char typ;
        int a, b;
        cin >> typ >> a >> b;
        a--;
        b--;
        if (typ == 'Q'){
            int naj_0 = 0;
            int naj_1 = 0;
            int akt_0 = 0;
            int akt_1 = 0;
            char pop;
            for (int i = a; i <= b; i++){
                if (tab[i] != pop){
                    if (tab[i] == '0'){
                        naj_0 = max(naj_0, akt_0);
                        akt_0 = 1;
                    } else {
                        naj_1 = max(naj_1, akt_1);
                        akt_1 = 1;
                    }
                } else {
                    if (tab[i] == '0'){
                        akt_0++;
                    } else {
                        akt_1++;
                    }
                }
                pop = tab[i];
            }
            naj_0 = max(naj_0, akt_0);
            naj_1 = max(naj_1, akt_1);
            cout << max(naj_1, naj_0) << '\n';
        } else {
            char temp = tab[a];
            tab[a] = tab[b];
            tab[b] = temp;
        }
    }

    return 0;
}
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 2e5 + 5;
//const int MAXN = 6;
ll pref[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;

    pref[0] = 0;
    for (int i = 1; i <= n; i++){
        ll x;
        cin >> x;
        pref[i] = pref[i - 1] + x;
    }

    for (int i = 0; i < q; i++){
        int start;
        ll ile;
        cin >> start >> ile;
        ll na_lewo = pref[start];
        ll na_prawo = pref[n] - pref[start - 1];
        if (na_lewo >= ile){
            int pocz = 1;
            int kon = start;
            while (pocz < kon){
                int srodek = (pocz + kon) / 2;
                ll kon_suma = pref[start];
                ll pocz_suma = pref[srodek - 1];
                ll suma = kon_suma - pocz_suma;
                if (suma > ile){
                    pocz = srodek;
                } else {
                    kon = srodek - 1;
                }
            }
            cout << start - pocz + 1 << '\n';
        } else if (na_prawo >= ile){
            int pocz = start;
            int kon = n;
            while (pocz < kon){
                int srodek = (pocz + kon) / 2;
                ll kon_suma = pref[srodek];
                ll pocz_suma = pref[start - 1];
                ll suma = kon_suma - pocz_suma;
                if (suma > ile){
                    kon = srodek;
                } else {
                    pocz = srodek + 1;
                }
            }
            cout << kon - start + 1 << '\n';
        } else {
            cout << "NIE" << endl;
        }
    }

    return 0;
}

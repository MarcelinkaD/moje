//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/dwa/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1e6 + 5;
ll pod = 31;
ll MOD = 1e9 + 21;
ll hasz1[MAXN];
ll hasz2[MAXN];
ll pot[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    string s1, s2;
    cin >> s1 >> s2;

    pot[0] = 1;
    for (int i = 1; i <= max(n, m); i++){
        pot[i] = (pot[i - 1] * pod) % MOD;
    }

    s1 = '?' + s1;
    for (int i = 1; i <= n; i++){
        hasz1[i] = (hasz1[i - 1] + ((s1[i] - 'a' + 1) * pot[i])) % MOD;
    }

    s2 = '?' + s2;
    for (int i = 1; i <= m; i++){
        hasz2[i] = (hasz2[i - 1] + ((s2[i] - 'a' + 1) * pot[i])) % MOD;
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; i++){
        int pocz1, kon1, pocz2, kon2;
        cin >> pocz1 >> kon1 >> pocz2 >> kon2;
        if (kon1 - pocz1 == kon2 - pocz2){
            ll war1 = (hasz1[kon1] - hasz1[pocz1 - 1] + MOD) % MOD;
            ll war2 = (hasz2[kon2] - hasz2[pocz2 - 1] + MOD) % MOD;
            if (pocz1 < pocz2){
                war1 = (war1 * pot[pocz2 - pocz1]) % MOD;
            }
            else if (pocz2 < pocz1){
                war2 = (war2 * pot[pocz1 - pocz2]) % MOD;
            }

            if (war1 == war2){
                cout << "TAK" << endl;
            }
            else{
                cout << "NIE" << endl;
            }
        } else {
            cout << "NIE" << endl;
        }
    }

    return 0;
}

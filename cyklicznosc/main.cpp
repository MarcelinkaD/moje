//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/cyk/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int pod = 313;
const ll MOD = 1e9 + 21;
const int MAXN = 2e6 + 5;
ll hasz1[MAXN];
ll hasz2[MAXN];
ll pot[MAXN];

bool porownaj(int p1, int k1, int p2, int k2){
    ll h1, h2;
    if (k1 - p1 != k2 - p2){
        return 0;
    }
    h1 = (hasz1[k1] - hasz1[p1 - 1] + MOD) % MOD;
    h2 = (hasz2[k2] - hasz2[p2 - 1] + MOD) % MOD;

    if (p1 <= p2){
        h1 = (h1 * pot[p2 - p1]) % MOD;
    } else {
        h2 = (h2 * pot[p1 - p2]) % MOD;
    }
    return (h1 == h2);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    string s1, s2;
    cin >> n;
    cin >> s1 >> s2;
    s1 = s1 + s1;

    pot[0] = 1;
    for (int i = 1; i < n * 2; i++){
        pot[i] = (pot[i - 1] * pod) % MOD;
    }

    hasz1[0] = ((ll)(s1[0]) * pot[0]) % MOD;
    for (int i = 0; i < 2 * n; i++){
        hasz1[i] = (hasz1[i - 1] + ((ll)(s1[i]) * pot[i])) % MOD;
    }

    hasz2[0] = ((ll)(s2[0]) * pot[0]) % MOD;
    for (int i = 0; i < n; i++){
        hasz2[i] = (hasz2[i - 1] + ((ll)(s2[i]) * pot[i])) % MOD;
    }

    for (int i = 0; i < 2 * n; i++){
        if (porownaj(i, i + n - 1, 0, n - 1)){
            cout << "TAK" << endl;
            return 0;
        }
    }
    cout << "NIE" << endl;

    return 0;
}

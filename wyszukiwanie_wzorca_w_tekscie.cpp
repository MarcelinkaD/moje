#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 4e7 + 5;
const int pod = 313;
const int mod = 1e9 + 21;
ll hasz1[MAXN];
ll pot[MAXN];
ll hasz2;

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

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    string s1, s2;
    cin >> s1 >> s2;

    pot[0] = 1;
    for (int i = 1; i < n; i++){
        pot[i] = (pot[i - 1] * pod) % mod;
    }

    hasz1[0] = ((ll)(s1[0]) * pot[0]) % mod;
    for (int i = 0; i < 2 * n; i++){
        hasz1[i] = (hasz1[i - 1] + ((ll)(s1[i]) * pot[i])) % mod;
    }
    
    hasz2[0] = ((ll)(s2[0]) * pot[0]) % mod;
    for (int i = 0; i < n; i++){
        hasz2[i] = (hasz2[i - 1] + ((ll)(s2[i]) * pot[i])) % mod;
    }

    int w = 0;
    for (int i = 0; i < n - m; i++){
        if (porownaj(i, i + m - 1, 0, m - 1)){
            w++;
        }
    }
    cout << w << endl;

    return 0;
}
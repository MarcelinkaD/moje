#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MOD = 1e9 + 7;

ll potega(ll a, ll b){
    ll wyn = 1;
    while (b > 0){
       if (b % 2 == 1){
            wyn = (wyn * a) % MOD;
        }
        a = (a * a) % MOD;
        b /= 2;
    }
    return wyn;
}

ll odw(ll x){
    return potega(x, MOD - 2);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    ll wszystkie = 1;
    for (int i = 2; i <= 2 * n; i++){
        wszystkie = (wszystkie * i) % MOD;
    }

    ll reszta = potega(2, n);
    ll odwrot = odw(reszta);

    ll wyn = (wszystkie * odwrot) % MOD;
    cout << wyn << endl;

    return 0;
}

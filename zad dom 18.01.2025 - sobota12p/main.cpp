// 1) https://cses.fi/problemset/task/2413
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MOD = 1e9 + 7;
unordered_map<int, ll> wyniki;

ll oblicz(int h){
    int pot = 1;
    while (h - 1 > 0){
        pot *= 3;
        h--;
    }
    return 1 + pot;
}

int main()
{
    int q;
    cin >> q;

    wyniki[1] = 2;
    for (int i = 0; i < q; i++){
        int n;
        cin >> n;
        if (wyniki.find(n) != wyniki.end()){
            cout << wyniki[n] % MOD << endl;
            continue;
        }
        for (int k = 1; k < n; k++){
            int H = n - k;
            for (int i = 0; i < n; i++){
                wyniki[n] += (oblicz(H) * wyniki[n - H]) % MOD;
            }
        }
        cout << wyniki[n] % MOD << endl;

    }

    return 0;
}

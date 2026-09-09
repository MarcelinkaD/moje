#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<ll> tab(n);

    for (int i = 0; i < n; i++){
        cin >> tab[i];
    }

    ll wyn = 0;
    for (int i = n - 1; i > 0; i--){
        if (tab[i - 1] > tab[i]){
            wyn += tab[i - 1] - tab[i];
            tab[i - 1] -= tab[i - 1] - tab[i];
        }
    }
    cout << wyn << '\n';

    return 0;
}
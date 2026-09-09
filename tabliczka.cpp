#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;
    while (q--){
        ll a, b;
        cin >> a >> b;
        ll m = max(a, b);
        if (m % 2 == 0){
            if (a <= b){
                cout << (m - 1) * (m - 1) + a << '\n';
            } else {
                cout << m * m - (b - 1) << '\n';
            }
        } else {
            if (a <= b){
                cout << m * m - (a - 1) << '\n';
            } else {
                cout << (m - 1) * (m - 1) + b << '\n';
            }
        }
    }

    return 0;
}
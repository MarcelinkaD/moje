#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;
    while (q--){
        ll a, b, x, y;
        cin >> a >> b >> x >> y;
        if (a > b){
            if (a - b == 1 && a % 2 == 1){
                cout << y << '\n';
            } else {
                cout << -1 << '\n';
            }
        } else if (a < b) {
            ll roznica = b - a;
            ll ile_xor = 0;
            if (roznica % 2 == 1){
                if (a % 2 == 0){
                    ile_xor = (roznica / 2) + 1;
                } else {
                    ile_xor = (roznica / 2);
                }
            } else {
                ile_xor = (roznica / 2);
            }
            ll z_xor = ile_xor * y + (roznica - ile_xor) * x;
            ll bez_xor = roznica * x;
            cout << min(z_xor, bez_xor) << '\n';
        } else {
            cout << 0 << '\n';
        }
    }

    return 0;
}
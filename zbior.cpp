#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ll n;
    cin >> n;

    ll suma = (n * (n + 1)) / 2;
    
    if ((suma / 2) * 2 == suma){
        cout << "TAK" << '\n';
        vector<int> pierw_zb;
        vector<int> dru_zb;
        ll s1 = 0;
        ll s2 = 0;
        for (int i = n; i > 0; i--){
            if (min(s1, s2) == s1){
                s1 += i;
                pierw_zb.push_back(i);
            } else {
                s2 += i;
                dru_zb.push_back(i);
            }
        }
        cout << pierw_zb.size() << '\n';
        for (auto i : pierw_zb){
            cout << i << ' ';
        }
        cout << '\n';
        cout << dru_zb.size() << '\n';
        for (auto i : dru_zb){
            cout << i << ' ';
        }
    } else {
        cout << "NIE" << '\n';
    }

    return 0;
}
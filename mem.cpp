#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

struct frag {
    string ciag;
    ll x = 0, d = 0, smiesz = 0;
};

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<frag> kaw;

    for (int i = 0; i < n; i++){
        string s;
        cin >> s;
        ll ilex = 0, iled = 0;
        ll smie = 0;
        for (int k = (int)s.size() - 1; k >= 0; k--){
            if (s[k] == 'D'){
                iled++;
            } else if (s[k] == 'x'){
                ilex++;
                smie += iled;
            }
        }
        frag x;
        x.ciag = s;
        x.d = iled;
        x.x = ilex;
        x.smiesz = smie;
        kaw.push_back(x);
    }

    sort(kaw.begin(), kaw.end(), [](const frag& a, const frag& b){
        if (a.x * b.d != b.x * a.d) {
            return a.x * b.d > b.x * a.d; 
        }
        return a.d < b.d;              
    });

    ll pop_x = 0;
    ll wyn = 0;
    for (auto i : kaw){
        wyn += i.smiesz + pop_x * i.d;
        pop_x += i.x;
    }

    cout << wyn << '\n';

    return 0;
}
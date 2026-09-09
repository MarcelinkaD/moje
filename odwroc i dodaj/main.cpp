//https://szkopul.edu.pl/problemset/problem/xorpERQu25Ex5Z6l64izA6XK/site/?key=statement
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll odwr(ll x){
    ll wyn = 0, r;
    while (x != 0){
        r = x % 10;
        wyn *= 10;
        wyn += r;
        x /= 10;
    }
    return wyn;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int q;
    cin >> q;

    while (q){
        ll n;
        cin >> n;
        int w = 0;
        ll akt_w = n;

        if (n != odwr(n)){
            while (true){
                ll nowe_n = odwr(akt_w);
                akt_w += nowe_n;
                w++;
                if (akt_w == odwr(akt_w)){
                    break;
                }
            }
        }
        cout << w << ' ' << akt_w << endl;
        q--;
    }

    return 0;
}

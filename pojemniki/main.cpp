//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/poj/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

vector<ll> male;
vector<ll> duze;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    ll k, x, m, d;
    cin >> n;
    cin >> k;

    for (int i = 0; i < n; i++){
        cin >> x;
        if (x <= k) {
            male.push_back(x);
        } else {
            duze.push_back(x);
        }
    }

    while (!male.empty() && !duze.empty()){
        m = male.back();
        d = duze.back();
        male.pop_back();
        duze.pop_back();
        d -= (k - m);
        if (d > k) {
            duze.push_back(d);
        } else {
            male.push_back(m);
        }
    }
    if (duze.empty()){
        cout << "TAK" << "\n";
    } else {
        cout << "TAK" << "\n";
    }

    return 0;
}

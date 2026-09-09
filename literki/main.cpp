#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const ll R = (1 << 23) + 6;
ll M = 1 << 22;
ll drzewo[R];

void add(ll x) {
    x += M;
    while (x > 0) {
        drzewo[x] += 1;
        x >>= 1;
    }
}

void usun(ll x) {
    x += M;
    while (x > 0) {
        drzewo[x] -= 1;
        x >>= 1;
    }
}

ll query(ll a, ll b) {
    ll w = 0;
    a += M;
    b += M;
    w = drzewo[a];
    if (a != b)
    w += drzewo[b];
    while ((a >> 1) != (b >> 1)) {
        if (a % 2 == 0)
            w += drzewo[a + 1];
        if (b % 2 == 1)
            w += drzewo[b - 1];
        a >>= 1;
        b >>= 1;
    }
    return w;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll n;
    cin >> n;

    string a;
    string b;
    cin >> a >> b;
    reverse(b.begin(), b.end());
    string koniec = a + b;
    vector<stack<ll>> index(256, stack<ll>());
    ll res = 0;
    for (ll i = 0; i < 2 * n; i++) {
        if (i < n) {
            add(i);
            index[koniec[i]].push(i);
        }
        if (i >= n) {
            usun(index[koniec[i]].top());
            ll sum = query(index[koniec[i]].top(), i);
            index[koniec[i]].pop();
            res += sum;
        }
    }


    cout << res << '\n';
}

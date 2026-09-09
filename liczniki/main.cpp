//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/lic/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

vector<pair<ll, ll>> akt_stan;
multiset<ll> worek;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    ll wyn = 0;

    for (int i = 0; i < n; i++){
        pair<ll, ll> x;
        cin >> x.first;
        akt_stan.push_back(x);
    }

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        akt_stan[i].second = x;
    }

    sort(akt_stan.begin(), akt_stan.end(), [](const pair<ll, ll>& a, const pair<ll, ll>& b) {
        return a.first > b.first;
    });

    for (int k = 0; k < m; k++){
        for (int i = 0; i < n; i++){
            int x;
            cin >> x;
            worek.insert(x);
        }
        for (int i = 0; i < n; i++){
            ll akt = akt_stan[i].second;
            auto op = worek.lower_bound(akt);
            if (op == worek.end()) {
                cout << "NIE" << endl;
                return 0;
            }
            ll nowy = *op;
            wyn += (nowy - akt) * akt_stan[i].first;
            akt_stan[i].second = nowy;
            worek.erase(op);
        }
    }
    cout << wyn << endl;

    return 0;
}

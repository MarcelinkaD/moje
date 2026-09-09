#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const ll MAXN = 5e5 + 5;
const ll L = 20;
vector<pair<ll, ll>> graf[MAXN];
pair<ll, ll> jp[MAXN][L]; // pzrodek, max z krawedzi
ll glebokosc[MAXN];
bool czy_odw[MAXN];

void wyznacz_ojca(ll akt_wie) {
    czy_odw[akt_wie] = 1;
    for (auto wierz : graf[akt_wie]){
        ll sasiad = wierz.first;
        ll kraw = wierz.second;
        if (!czy_odw[sasiad]){
            glebokosc[sasiad] = glebokosc[akt_wie] + 1;
            jp[sasiad][0].first = akt_wie;
            jp[sasiad][0].second = kraw;
            wyznacz_ojca(sasiad);
        }
    }
}

ll lca(ll u, ll v) {
    ll max_wyn = LLONG_MIN;
    if (glebokosc[u] > glebokosc[v]) {
        swap(v, u);
    }
    for (ll i = L - 1; i >= 0; i--) {
        if (glebokosc[jp[v][i].first] >= glebokosc[u]) {
            max_wyn = max(max_wyn, jp[v][i].second);
            v = jp[v][i].first;
        }
    }

    if (u == v) {
        return max_wyn;
    }

    for (ll i = L - 1; i >= 0; i--) {
        if (u == v) {
            return max_wyn;
        }
        if (jp[u][i].first != jp[v][i].first) {
            max_wyn = max(max_wyn, jp[v][i].second);
            max_wyn = max(max_wyn, jp[u][i].second);
            u = jp[u][i].first;
            v = jp[v][i].first;
        }
    }

    return max(max_wyn, max(jp[u][0].second, jp[v][0].second));
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ll n;
    cin >> n;

    for (ll i = 0; i < n - 1; i++){
        ll a, b, c;
        cin >> a >> b >> c;
        c += 1e9;
        graf[a].push_back({b, c});
        graf[b].push_back({a, c});
    }

    glebokosc[1] = 1;
    jp[1][0].first = 1;
    jp[1][0].second = LLONG_MIN;
    wyznacz_ojca(1);

    for (ll j = 1; j < L; j++){
        for (ll i = 1; i <= n; i++){
            jp[i][j].first = jp[jp[i][j - 1].first][j - 1].first;
            jp[i][j].second = max(jp[jp[i][j - 1].first][j - 1].second, jp[i][j - 1].second);
            if (jp[i][j].first == 0) {
                jp[i][j].first = 1;
            }
        }
    }

    while (true){
        ll a, b;
        cin >> a;
        if (a == -1){
            break;
        } else {
            cin >> b;
            ll wyn = lca(a, b);
            if (wyn == LLONG_MIN){
                cout << 0 << endl;
            } else {
                cout << wyn - (ll)1e9 << endl;
            }
        }
    }

    return 0;
}

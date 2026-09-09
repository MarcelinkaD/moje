//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/dijkstra/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1e6 + 5;
const ll INF = 1e18;
vector<pair<int, int>> graf[MAXN];
vector<pair<int, int>> graf_odw[MAXN];
ll odl[MAXN];
pair<int, ll> pop[MAXN];

void dijkstra1() {
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> kol;

    for (int i = 0; i < MAXN; i++) {
        odl[i] = INF;
        pop[i].first = -1;
    }

    odl[1] = 0;
    kol.push({0, 1});

    while (!kol.empty()) {
        int u = kol.top().second;
        ll d = kol.top().first;
        kol.pop();
        if (d > odl[u]) continue;
        for (auto [sasiad, droga] : graf[u]) {
            if (odl[sasiad] > droga + odl[u]) {
                odl[sasiad] = droga + odl[u];
                pop[sasiad].first = u;
                pop[sasiad].second = odl[sasiad];
                kol.push({odl[sasiad], sasiad});
            }
        }
    }
}

void dijkstra2() {
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> kol;

    for (int i = 0; i < MAXN; i++) {
        odl[i] = INF;
        pop[i].first = -1;
    }

    odl[1] = 0;
    kol.push({0, 1});

    while (!kol.empty()) {
        int u = kol.top().second;
        ll d = kol.top().first;
        kol.pop();
        if (d > odl[u]) continue;
        for (auto [sasiad, droga] : graf_odw[u]) {
            if (odl[sasiad] > droga + odl[u]) {
                odl[sasiad] = droga + odl[u];
                pop[sasiad].first = u;
                pop[sasiad].second = odl[sasiad];
                kol.push({odl[sasiad], sasiad});
            }
        }
    }
}

void zmien_graf(const vector<pair<int, int>> &sciezka) {
    for (int i = 0; i < sciezka.size() - 1; i++) {
        int a = sciezka[i].first;
        int b = sciezka[i + 1].first;
        int c = sciezka[i + 1].second - sciezka[i].second;
        for (auto it = graf_odw[a].begin(); it != graf_odw[a].end(); ++it) {
            if (it->first == b) {
                graf_odw[a].erase(it);
                break;
            }
        }
        graf_odw[b].push_back({a, -c});
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    ll wyn = 0;

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graf[a].push_back({b, c});
        graf_odw[a].push_back({b, c});
    }

    dijkstra1();
    wyn += odl[n];

    if (odl[n] == INF) {
        cout << -1 << endl;
        return 0;
    }

    vector<pair<int, int>> s1;
    int v = n;
    int d = pop[n].second;
    while (v != -1) {
        s1.push_back({v, d});
        v = pop[v].first;
        d = pop[v].second;
    }
    reverse(s1.begin(), s1.end());
    set<tuple<int, int, ll>> set1;

    for (int i = 0; i < s1.size() - 1; i++) {
        int a = s1[i].first;
        int b = s1[i + 1].first;
        ll c = s1[i + 1].second - s1[i].second;
        set1.insert({a, b, c});
    }

    zmien_graf(s1);

    dijkstra2();
    wyn += odl[n];

    vector<pair<int, int>> s2;
    int v = n;
    int d = pop[n].second;
    while (v != -1) {
        s2.push_back({v, d});
        v = pop[v].first;
        d = pop[v].second;
    }
    reverse(s2.begin(), s2.end());
    set<tuple<int, int, ll>> set2;
    for (int i = 0; i < s1.size() - 1; i++) {
        int a = s2[i].first;
        int b = s2[i + 1].first;
        ll c = s2[i + 1].second - s2[i].second;
        if (c < 0){
            set2.insert({b, a, -c});
        } else {
            set2.insert({a, b, c});
        }
    }
    return 0;
}


//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r1e/
#include <bits/stdc++.h>
#define ll long long
using namespace std;

struct krawedz {
    int a, b;
    ll c;
    int ind;
    bool czy_znana;
};

struct hashFunction{
    size_t operator()(const pair<ll, ll> &x) const
  {
    return x.first * (2*1e9) + x.second;
  }
};

const int MAXN = 1e5 + 5;
const ll INF = 1e9 + 7;
vector<pair<int, pair<int, bool>>> graf[MAXN];
ll odl[MAXN];
vector<krawedz> krawedzie;
priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> kol;
pair<int, bool> poprzedni[MAXN];
unordered_set<pair<ll, ll>, hashFunction> uzyte;

void dijkstra(int od) {
    odl[od] = 0;
    kol.push({0, od});

    while (!kol.empty()){
        int u = kol.top().second;
        kol.pop();

        for (int i = 0; i < graf[u].size(); i++){
            int sasiad = graf[u][i].first;
            long long droga = graf[u][i].second.first;
            if (odl[sasiad] > odl[u] + droga) {
                odl[sasiad] = odl[u] + droga;
                poprzedni[sasiad].first = u;
                if (!graf[u][i].second.second) {
                    poprzedni[sasiad].second = false;
                } else {
                    poprzedni[sasiad].second = true;
                }

                kol.push({odl[sasiad], sasiad});
            }
        }
    }

}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    ll t;
    cin >> n >> m;
    cin >> t;

    for (int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        krawedz kra;
        kra.a = a;
        kra.b = b;
        if (c == -1) {
            kra.c = 1;
            kra.czy_znana = 0;
            graf[a].push_back({b, {1, false}});
        } else {
            kra.c = c;
            kra.czy_znana = 1;
            graf[a].push_back({b, {c, true}});
        }
        kra.ind = i;
        krawedzie.push_back(kra);
    }

    for (int i = 1; i <= n; i++) {
        odl[i] = INF;
    }

    dijkstra(1);
    ll min_dlugosc = odl[n];
    if (min_dlugosc == INF) {
        cout << -1 << endl;
        return 0;
    } else if (min_dlugosc == t) {
        for (int i = 0; i < m; i++){
            krawedz kra = krawedzie[i];
            cout << kra.c << endl;
        }
        return 0;
    } else if (min_dlugosc > t) {
        cout << -1 << endl;
        return 0;
    } else if (min_dlugosc < t) {
        int ile_nieznanych = 0;
        int akt_wie = n;
        bool czy_znany;
        int pop_wie;
        while (akt_wie != 1) {
            czy_znany = poprzedni[akt_wie].second;
            pop_wie = akt_wie;
            akt_wie = poprzedni[akt_wie].first;
            if (!czy_znany) {
                ile_nieznanych++;
                uzyte.insert({akt_wie, pop_wie});
            }
        }
        uzyte.insert({akt_wie, pop_wie});
        if (ile_nieznanych == 0) {
            cout << -1 << endl;
            return 0;
        }
        ll ile_przypadnie = (t - (min_dlugosc - ile_nieznanych)) / ile_nieznanych;
        if (ile_przypadnie <= 1e9) {
            if (ile_przypadnie * ile_nieznanych + (min_dlugosc - ile_nieznanych) == t) {
                for (int i = 0; i < m; i++){
                    krawedz kra = krawedzie[i];
                    pair<int, int> kraw = {kra.a, kra.b};
                    if (uzyte.find(kraw) != uzyte.end()) {
                        if (!kra.czy_znana) {
                            krawedzie[i].c = ile_przypadnie;
                        }
                    } else {
                        if (!kra.czy_znana) {
                            krawedzie[i].c = 1000000000;
                        }
                    }
                }
            } else {
                ll reszta = t - (ile_przypadnie * ile_nieznanych);
                bool czy_reszta_dana = 0;

                for (int i = 0; i < m; i++){
                    krawedz kra = krawedzie[i];
                    pair<int, int> kraw = {kra.a, kra.b};
                    if (uzyte.find(kraw) != uzyte.end()) {
                        if (!kra.czy_znana) {
                            if (!czy_reszta_dana) {
                                if (ile_przypadnie + reszta <= 1e9) {
                                    krawedzie[i].c = ile_przypadnie + reszta;
                                } else {
                                    cout << -1 << endl;
                                    return 0;
                                }
                            } else {
                                krawedzie[i].c = ile_przypadnie;
                            }
                        }
                    } else {
                        if (!kra.czy_znana) {
                            krawedzie[i].c = 1000000000;
                        }
                    }
                }
            }
        } else {
            cout << -1 << endl;
            return 0;
        }
    }

    for (int i = 0; i < m; i++){
        krawedz kra = krawedzie[i];
        cout << kra.c << endl;
    }

    return 0;
}

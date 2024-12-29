// 1) https://cses.fi/problemset/task/2106
#include <bits/stdc++.h>
using namespace std;

const pair<int, int> p = {31, 37};
const pair<long long, long long> mod = {1e9 - 63, 1e9 - 71};
const long long MAXN = 1e5 + 5;

long long hasz[MAXN][2], pot[MAXN][2];
int n;

pair<long long, long long> haszowanie(int pocz, int kon){
    return {(hasz[kon][0] - hasz[pocz - 1][0] + mod.first) * pot[n - kon][0] % mod.first, (hasz[kon][1] - hasz[pocz - 1][1] + mod.second) * pot[n - kon][1] % mod.second};
}

pair<int, int> czy_da_sie(int m) {
    if (m == 0 || m > n){
        return {-1, -1};
    }
    set<pair<long long, long long>> czy_bylo;
    for (int i = 1; i <= n - m; i++){
        pair<long long, long long> hasz_odc = haszowanie(i, i + m);
        if (czy_bylo.find(hasz_odc) != czy_bylo.end()) {
            return {i, i + m};
        }
        czy_bylo.insert(hasz_odc);
    }
    return {-1, -1};

}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string s;
    cin >> s;

    n = s.length();
    string text = '?' + s;
    pot[0][0] = 1;
    pot[0][1] = 1;
    for (int i = 1; i <= n; i++){
        pot[i][0] = (pot[i - 1][0] * p.first) % mod.first;
        pot[i][1] = (pot[i - 1][1] * p.second) % mod.second;
        hasz[i][0] = (hasz[i - 1][0] + (text[i] - 'a' + 1) * pot[i][0]) % mod.first;
        hasz[i][1] = (hasz[i - 1][1] + (text[i] - 'a' + 1) * pot[i][1]) % mod.second;
    }

    pair<int, int> naj_w = {-1, -1};
    int pocz = 1, kon = n - 1;
    while (pocz < kon) {
        int srodek = (pocz + kon) / 2;
        pair<int, int> w = czy_da_sie(srodek);
        if (w.first != -1) {
            naj_w = w;
            pocz = srodek + 1;
        } else {
            kon = srodek;
        }
    }

    if (naj_w.first != -1) {
        for (int i = naj_w.first; i <= naj_w.second; i++){
            cout << text[i];
        }
    } else {
        cout << -1 << endl;
    }

    return 0;
}

//https://cses.fi/problemset/task/1111
#include <bits/stdc++.h>
using namespace std;

const pair<int, int> p = {31, 37};
const pair<long long, long long> mod = {1000000007, 1000000033};
const long long MAXN = 1e6 + 5;

long long hasz_lewo[MAXN][2], pot_lewo[MAXN][2];
long long hasz_prawo[MAXN][2], pot_prawo[MAXN][2];
int n;

long long haszowanie_lewo(int pocz, int kon, int idx) {
    return ((hasz_lewo[kon][idx] - hasz_lewo[pocz - 1][idx] + mod.first) * pot_lewo[n - kon][idx] % mod.first);
}

long long haszowanie_prawo(int pocz, int kon, int idx) {
    return ((hasz_prawo[pocz][idx] - hasz_prawo[kon + 1][idx] + mod.first) * pot_prawo[pocz - 1][idx] % mod.first);
}

pair<int, int> czy_da_sie(int m) {
    if (m == 0 || m > n) {
        return {-1, -1};
    }

    for (int i = 1; i <= n - m + 1; i++) {
        long long hasz_odc_lewo_1 = haszowanie_lewo(i, i + m - 1, 0);
        long long hasz_odc_prawo_1 = haszowanie_prawo(i, i + m - 1, 0);
        long long hasz_odc_lewo_2 = haszowanie_lewo(i, i + m - 1, 1);
        long long hasz_odc_prawo_2 = haszowanie_prawo(i, i + m - 1, 1);

        if (hasz_odc_lewo_1 == hasz_odc_prawo_1 && hasz_odc_lewo_2 == hasz_odc_prawo_2) {
            return {i, i + m};
        }
    }
    return {-1, -1};
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string s;
    cin >> s;

    n = s.length();
    s = '?' + s;

    pot_lewo[0][0] = 1;
    pot_lewo[0][1] = 1;
    for (int i = 1; i <= n; i++) {
        pot_lewo[i][0] = (pot_lewo[i - 1][0] * p.first) % mod.first;
        pot_lewo[i][1] = (pot_lewo[i - 1][1] * p.second) % mod.second;
        hasz_lewo[i][0] = (hasz_lewo[i - 1][0] + (s[i] - 'a' + 1) * pot_lewo[i][0]) % mod.first;
        hasz_lewo[i][1] = (hasz_lewo[i - 1][1] + (s[i] - 'a' + 1) * pot_lewo[i][1]) % mod.second;
    }

    pot_prawo[n + 1][0] = 1;
    pot_prawo[n + 1][1] = 1;
    for (int i = n; i > 0; i--) {
        pot_prawo[i][0] = (pot_prawo[i + 1][0] * p.first) % mod.first;
        pot_prawo[i][1] = (pot_prawo[i + 1][1] * p.second) % mod.second;
        hasz_prawo[i][0] = (hasz_prawo[i + 1][0] + (s[i] - 'a' + 1) * pot_prawo[i][0]) % mod.first;
        hasz_prawo[i][1] = (hasz_prawo[i + 1][1] + (s[i] - 'a' + 1) * pot_prawo[i][1]) % mod.second;
    }

    pair<int, int> naj_w;
    for (int i = n; i >= 1; i--) {
        naj_w = czy_da_sie(i);
        if (naj_w.first != -1) {
            break;
        }
    }

    if (naj_w.first != -1) {
        for (int i = naj_w.first; i < naj_w.second; i++) {
            cout << s[i];
        }
    } else {
        cout << -1 << endl;
    }

    return 0;
}

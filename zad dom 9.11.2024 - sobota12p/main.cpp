// 1) https://cses.fi/problemset/task/1753
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1;
    cin >> s2;

    if (s2.size() > s1.size()) {
        cout << 0;
        return 0;
    }

    long long hasz_s1 = 0, hasz_s2 = 0, pot = 1, w = 0;
    int pod = 31;
    int mod = 1e9 - 63;

    for (int i = 0; i < s2.size(); i++) {
        hasz_s2 = (hasz_s2 + s2[i] * pot) % mod;
        hasz_s1 = (hasz_s1 + s1[i] * pot) % mod;

        if (i < s2.size() - 1) {
            pot = (pot * pod) % mod;
        }
    }

    if (hasz_s1 == hasz_s2) {
        w++;
    }

    for (int i = s2.size(); i < s1.size(); i++) {
        hasz_s1 = (hasz_s1 - (s1[i - s2.size()] * pot) % mod + mod) % mod;
        hasz_s1 = (hasz_s1 + s1[i] * pot) % mod;
        pot = (pot * pod) % mod;

        if (hasz_s1 == hasz_s2) {
            w++;
        }
    }

    cout << w << endl;

    return 0;
}


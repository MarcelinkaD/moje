#include <bits/stdc++.h>
using namespace std;

const int POW = 131;
const int MOD = 10000007;

int main() {
    int t; cin >> t;
    while (t--) {
        string s; cin >> s;
        int n = s.size();
        vector<vector<int>> hashe(s.size(), vector<int>(s.size(), 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j ++) {
                if (j < i)
                    continue;
                if (i == j) {
                    hashe[i][j] = s[i];
                    continue;
                }
                hashe[i][j] = (hashe[i][j - 1] * POW + s[j]) % MOD;
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j --) {
                if (i < j)
                    continue;
                if (i == j) {
                    hashe[i][j] = s[i];
                    continue;
                }
                hashe[i][j] = (hashe[i][j + 1] * POW + s[j]) % MOD;
            }
        }

        int lewo = 0, prawo = n-1;
        while (true) {
            
            bool done = false;
            if (lewo == prawo - 1) {
                if (hashe[lewo][lewo] == hashe[prawo][prawo]) {
                    lewo ++;
                    break;
                }
            }
            for (int srodek = (lewo + prawo) / 2; srodek > 0; srodek --) {
                int rel = srodek - lewo;
                if (hashe[lewo][rel + lewo - 1] == hashe[2 * rel - 1 + lewo][rel + lewo]) {
                    lewo += srodek;
                    done = true;
                    break;
                }
                if (hashe[prawo - rel + 1][prawo] == hashe[prawo - 2 * rel + 1][prawo - rel]) {
                    prawo -= srodek;
                    done = true;
                    break;
                }
            }
            if (!done)
                break;

            /*
            for (int i = 0; i < n / 2; i++) {
                if (hashe[0][i - 1] == hashe[2 * i - 1][i]) {
                    n = 
                }
            }
            */
        }
        cout << prawo - lewo + 1 << '\n';
    }
}
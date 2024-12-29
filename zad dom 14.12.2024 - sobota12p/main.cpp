// 1) https://cses.fi/problemset/task/1638
/*#include <iostream>
using namespace std;

const int MAXN = 1005;
const int MOD = 1e9 + 7;
int dp[MAXN][MAXN];

bool inRange(int a, int b) {
    return ((a >= 0 && b >= 0) && dp[a][b] != -1);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            char x;
            cin >> x;
            if (x == '*') {
                dp[i][k] = -1;
            }
        }
    }

    if (dp[0][0] != -1) {
        dp[0][0] = 1;
    } else {
        cout << 0 << endl;
        return 0;
    }

    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            if (dp[i][k] == -1) continue;
            if (inRange(i - 1, k)){
                dp[i][k] += dp[i - 1][k] % MOD;
            }
            if (inRange(i, k - 1)){
                dp[i][k] += dp[i][k - 1] % MOD;
            }
        }
    }

    if (dp[n - 1][n - 1] != -1) {
        cout << dp[n - 1][n - 1] % MOD;
    } else {
        cout << 0 << endl;
        return 0;
    }

    return 0;
}*/

//2) https://szkopul.edu.pl/problemset/problem/sScTfpOMztxGKXrTY3RW15qy/site/?key=statement
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 2003;
int dp[MAXN][MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string s1, s2;
    cin >> s1 >> s2;
    int n = s1.size();
    int m = s2.size();

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
                continue;
            }
            char z1 = s1[i - 1], z2 = s2[j - 1];
            if (z1 == z2) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    cout << dp[n][m] << endl;

    return 0;
}

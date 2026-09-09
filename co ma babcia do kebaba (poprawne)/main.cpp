#include <bits/stdc++.h>
using namespace std;

const int MAXN = 5005;
int dp[MAXN][MAXN];
string wyn;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string s1, s2;
    cin >> s1 >> s2;

    int n = s1.size();
    int m = s2.size();

    s1 = '?' + s1;
    s2 = '#' + s2;

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            if (s1[i] == s2[j]){
                if (dp[i][j] < dp[i - 1][j - 1] + 1){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }
            }
        }
    }

    cout << dp[n][m] << endl;

    int i = n;
    int j = m;
    while (i != 0 && j != 0){
        if (dp[i - 1][j] == dp[i][j]){
            i--;
        } else if (dp[i][j - 1] == dp[i][j]) {
            j--;
        } else {
            wyn += s1[i];
            j--;
        }
    }

    for (int k = wyn.size() - 1; k >= 0; k--){
        cout << wyn[k];
    }

    return 0;
}

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
const int MAXB = 1e4 + 5;
int dp[MAXN][MAXB];
pair<int, int> przed[MAXN];
vector<int> odp;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, poj;
    cin >> n >> poj;

    for (int i = 1; i <= n; i++){
        cin >> przed[i].second;
    }

    for (int i = 1; i <= n; i++){
        cin >> przed[i].first;
    }

    for (int i = 0; i <= poj; i++){
        dp[0][i] = 0;
    }

    for (int i = 1; i <= n; i++){
        for (int j = 0; j <= poj; j++){
            dp[i][j] = dp[i - 1][j];
            if (j >= przed[i].second) {
                dp[i][j] = max(dp[i - 1][j - przed[i].second] + przed[i].first, dp[i][j]);
            }
        }
    }

    cout << dp[n][poj] << endl;

    int i = n;
    int j = poj;
    while (i > 0 && j > 0){
        if (j - przed[i].second >= 0){
            if (dp[i - 1][j] < dp[i][j - przed[i].second] + przed[i].first) {
                odp.push_back(i);
                j -= przed[i].second;
            }
        }
        i--;
    }

    cout << odp.size() << endl;
    for (auto i : odp){
        cout << i
         << ' ';
    }

    return 0;
}

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 5e4 + 5;
const int MAXK = 105;
bool w[MAXK][MAXN];
pair<int, int> dp[MAXK][MAXN];
pair<bool, bool> gdzie_grzyb[MAXN];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    int l, p;
    cin >> l >> p;

    for (int i = 0; i < l; i++) {
        int a;
        cin >> a;
        gdzie_grzyb[a].first = true;
    }

    for (int i = 0; i < p; i++) {
        int a;
        cin >> a;
        gdzie_grzyb[a].second = true;
    }

    for (int i = 0; i <= k; i++) {
        for (int j = 1; j <= n; j++) {
            if (i % 2 == 0){
                w[i][j] = gdzie_grzyb[j].first;
            } else {
                w[i][j] = gdzie_grzyb[j].second;
            }
        }
    }

    dp[0][1].first = (int)w[0][1];
    dp[0][1].second = (int)w[0][1];

    for (int i = 2; i <= n; i++)
        dp[0][i] = {0, dp[0][i - 1].second + (int)w[0][i]};

    for (int i = 1; i <= k; i++) {
        dp[i][1].first = dp[i - 1][1].second + w[i][1];
    }

    for (int i = 1; i <= k; i++) {
        for (int j = 2; j <= n; j++) {
            dp[i][j].first = dp[i - 1][j].second + w[i][j];
            dp[i][j].second = max(dp[i][j - 1].first, dp[i][j - 1].second) + w[i][j];
        }
    }

    int naj_w = 0;
    for (int i = 0; i <= k; i++) {
        naj_w = max(naj_w, max(dp[i][n].first, dp[i][n].second));
    }

    cout << naj_w << endl;
}

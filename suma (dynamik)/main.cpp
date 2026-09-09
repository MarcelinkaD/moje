#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1e6 + 5;
ll dp[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        ll x;
        cin >> x;
        if (i == 0){
            dp[i] = max((ll)0, x);
        } else if (i == 1){
            dp[i] = max(dp[i - 1], x);
        } else {
            dp[i] = max(dp[i - 2] + x, dp[i - 1]);
        }
    }

    cout << dp[n - 1] << endl;

    return 0;
}

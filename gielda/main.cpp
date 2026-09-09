//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/gie/
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int MAXN = 1e6 + 5;
ll tab[MAXN];
ll dp[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    ll x;
    cin >> n >> x;
    ll max_sum = -1e9 - 5;
    for (int i = 1; i <= n; i++){
        cin >> tab[i];
        dp[i] = max(dp[i - 1], tab[i] + max_sum);
        max_sum = max(max_sum, dp[i] - tab[i] - x);
    }
    cout << dp[n] << endl;
    return 0;
}

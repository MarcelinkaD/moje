//https://szkopul.edu.pl/c/konkurs-przed-obozem-oki-2025/p/pil/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
int pilki[MAXN][MAXN];
int dp[MAXN][MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; i++){
        for (int k = 1; k <= m; k++){
            cin >> pilki[i][k];
        }
    }

    for (int i = 1; i <= n; i++){
        for (int k = 1; k <= m; k++){
            dp[i][k] = max(dp[i - 1][k] + pilki[i][k], dp[i][k - 1] + pilki[i][k]);
        }
    }

    cout << dp[n][m] << endl;

    return 0;
}

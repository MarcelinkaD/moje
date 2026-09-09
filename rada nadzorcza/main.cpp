#include <bits/stdc++.h>
using namespace std;

const int MAXN = 50005;
bool dp[MAXN][360];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    dp[0][0] = 1;
    for (int i = 1; i <= n; i++){
        int x;
        cin >> x;
        for (int j = 0; j < 360; j++){
            if (dp[i - 1][j] == 0) continue;
            dp[i][(j + x + 360) % 360] = 1;
            dp[i][(j - x + 360) % 360] = 1;
        }
    }

    if (dp[n][0]){
        cout << "TAK" << endl;
    } else {
        cout << "NIE" << endl;
    }

    return 0;
}

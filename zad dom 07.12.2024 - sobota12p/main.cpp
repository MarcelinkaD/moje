// 1) Dany jest ci¹g liczb. Wybierz 3 liczby, aby ich suma by³a mo¿liwie najwiêksza, ale te liczby nie mog¹ byæ s¹siednie.
/*#include <iostream>
using namespace std;

const int MAXN = 1e6 + 5;
int dp[MAXN][3];
int l[MAXN];

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> l[i];
    }

    dp[0][0] = l[0];
    for (int i = 1; i < n; i++) {
        dp[i][0] = max(dp[i - 1][0], l[i]);
    }

    dp[0][1] = l[0];
    dp[0][2] = l[0];
    dp[1][1] = max(l[0], l[1]);
    dp[1][2] = max(l[0], l[1]);
    for (int i = 2; i < n; i++) {
        dp[i][1] = max(dp[i - 2][0] + l[i], dp[i - 1][1]);
        dp[i][2] = max(dp[i - 2][1] + l[i], dp[i - 1][2]);
    }

    cout << dp[n - 1][2] << endl;

    return 0;
}
*/

// 1*) Customowe K
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
int l[MAXN];
int dp[MAXN][100];

int main()
{
    int n, k;
    cin >> n >> k;

    if (k > n / 2) {
        cout << "nie da sie" << endl;
        return 0;
    }

    for (int i = 0; i < n; i++){
        cin >> l[i];
    }

    dp[0][0] = l[0];
    for (int i = 1; i < n; i++) {
        dp[i][0] = max(dp[i - 1][0], l[i]);
    }

    for (int i = 1; i < n; i++){
        for (int j = 1; j < k; j++){
            if (i - 2 < 0) {
                dp[i][j] = 0;
            } else {
                dp[i][j] = max(dp[i - 2][j - 1] + l[i], dp[i - 1][j - 1]);
            }
        }
    }

    cout << dp[n - 1][k - 1] << endl;

    return 0;
}

//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/saf/
#include <iostream>
using namespace std;

const int MAXN = 1e6 + 5;
long long dp[MAXN];
long long l[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> l[i];
    }

    dp[0] = l[0];
    dp[1] = max(l[0], l[1]);
    for (int i = 2; i < n; i++){
        dp[i] = max(dp[i - 1], dp[i - 2] + l[i]);
    }

    cout << dp[n - 1] << endl;

    return 0;
}

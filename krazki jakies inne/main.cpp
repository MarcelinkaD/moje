#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
//const int MAXN = 5;
int plansza[MAXN][MAXN];
bool czy_jest_na_lewo[MAXN][MAXN];
bool czy_bylo_dodanie[MAXN];
int dp[MAXN][MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            cin >> plansza[i][j];
        }
    }

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            czy_jest_na_lewo[i][j] = czy_jest_na_lewo[i][j - 1];
            if (plansza[i][j - 1] != 0) {
                czy_jest_na_lewo[i][j] = true;
            }
        }
    }

    for (int j = 1; j <= m; j++){
        dp[1][j] = (bool)plansza[1][j] || dp[1][j - 1];
    }

    for (int i = 1; i <= n; i++){
        dp[i][1] = (bool)plansza[i][1] || dp[i - 1][1];
    }

    for (int j = 2; j <= m; j++){
        for (int i = 2; i <= n; i++){
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            if (czy_jest_na_lewo[i][j] && !czy_bylo_dodanie[i]) {
                czy_bylo_dodanie[i] = true;
                dp[i][j]++;
            }
        }
    }
    cout << dp[n][m] << '\n';

    return 0;
}

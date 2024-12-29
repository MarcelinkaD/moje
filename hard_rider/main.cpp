//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/har/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
vector<int> graf[MAXN];
bool czy_odw[MAXN];
int dp[MAXN][2];

void max_zbior_niezal(int akt_wie) { // DFS!!!
    czy_odw[akt_wie] = 1;
    dp[akt_wie][1] = 1;
    dp[akt_wie][0] = 0;
    for (int i = 0; i < graf[akt_wie].size(); i++) {
        int sasiad = graf[akt_wie][i];
        if (!czy_odw[sasiad]) {
            max_zbior_niezal(sasiad);
            dp[akt_wie][1] += dp[sasiad][0];
            dp[akt_wie][0] += dp[sasiad][1];
        }
    }
    dp[akt_wie][1] = max(dp[akt_wie][1], dp[akt_wie][0]);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++){
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    max_zbior_niezal(1);
    cout << max(dp[1][1], dp[1][0]) << endl;
    return 0;
}

//https://szkopul.edu.pl/c/map-2024_2025/p/prz1/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 7;
int w[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;

    int maxi = 0;
    int mini_licz = 0;
    int ost_maxi = MAXN;
    int ost_guzik = n + 1;
    for (int i = 0; i < m; i++){
        int x;
        cin >> x;
        if (x != ost_guzik){
            if (ost_maxi < i && w[x] < mini_licz){
                w[x] = mini_licz + 1;
            } else {
                w[x]++;
            }
            if (w[x] > maxi) {
                maxi = w[x];
            }
        } else {
            ost_maxi = i;
            mini_licz = maxi;
        }
    }

    ostringstream output;
    for (int i = 1; i <= n; i++){
        if (w[i] < mini_licz){
            output << mini_licz << ' ';
        } else {
            output << w[i] << ' ';
        }
    }
    cout << output.str();

    return 0;
}

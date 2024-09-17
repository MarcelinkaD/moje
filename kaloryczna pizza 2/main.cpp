#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;
    vector<vector<long long>> sumy;

    sumy.resize(n + 1);

    for (int i = 0; i <= m; i++) {
        sumy[0].push_back(0);
    }

    for (int i = 1; i <= n; i++) {
        sumy[i].push_back(0);
        for (int k = 0; k < m; k++) {
            long long w;
            cin >> w;
            sumy[i].push_back(w);
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int k = 1; k <= m; k++) {
            sumy[i][k] = sumy[i][k - 1] + sumy[i - 1][k] + sumy[i][k] - sumy[i - 1][k - 1];
        }
    }

    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        int xl, yl, xp, yp;
        cin >> xl >> yl >> xp >> yp;
        cout << sumy[xp][yp] - sumy[xl - 1][yp] - sumy[xp][yl - 1] + sumy[xl - 1][yl - 1] << endl;
    }

    return 0;
}

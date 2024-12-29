//https://szkopul.edu.pl/c/map-2024_2025/p/opl/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
int l[MAXN][MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int a, b;
    cin >> a >> b;
    int c, d;
    cin >> c >> d;

    unordered_map<int, int> frag;
    frag[a]++;
    frag[b]++;
    frag[c]++;
    frag[d]++;

    int n, m;
    cin >> n >> n;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            int x;
            cin >> x;
            l[i][j] = x;
        }
    }

    if (n == 1 || m == 1) {
        cout << 0 << endl;
        return 0;
    }

    int w = 0;
    for (int i = 0; i < n - 2; i++){
        for (int j = 0; j < m - 2; j++){

        }
    }

}

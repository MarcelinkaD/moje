//https://szkopul.edu.pl/c/map-2024_2025/p/poc/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;
long long pref[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    pref[0] = 0;
    for (int i = 1; i <= n; i++){
        int x;
        cin >> x;
        pref[i] = x + pref[i - 1];
    }

    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << pref[b] - pref[a - 1] << endl;
    }

}

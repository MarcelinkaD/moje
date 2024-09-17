#include <iostream>
using namespace std;

const int MAXN = 1000007;
long long sumy_pref[MAXN] = {0};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, k, q;
    cin >> n >> k >> q;

    for (int i = 0; i < n; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        sumy_pref[a] += c;
        sumy_pref[b + 1] -= c;
    }

    for (int k = 1; k <= MAXN; k++) {
        sumy_pref[k] = sumy_pref[k - 1] + sumy_pref[k];
    }

    for (int j = 0; j < q; j++) {
        int x;
        cin >> x;
        cout << sumy_pref[x] << endl;
    }

    return 0;
}

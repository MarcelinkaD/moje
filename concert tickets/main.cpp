//https://cses.fi/alon/task/1091
#include <bits/stdc++.h>
using namespace std;

multiset<int> bilety;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        bilety.insert(x);
    }

for (int i = 0; i < m; i++){
        int x;
        cin >> x;

        if (bilety.empty()) {
            cout << -1 << endl;
            continue;
        }

        auto gdzie = bilety.lower_bound(x);

        if (gdzie == bilety.end() || *gdzie > x) {
            if (gdzie == bilety.begin()) {
                cout << -1 << endl;
            } else {
                --gdzie;
                cout << *gdzie << endl;
                bilety.erase(gdzie);
            }
        } else {
            cout << *gdzie << endl;
            bilety.erase(gdzie);
        }
    }

    return 0;
}

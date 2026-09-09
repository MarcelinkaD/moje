#include <bits/stdc++.h>

using namespace std;

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;

    set<int> punkty;

    char op;
    int x;
    for (int i = 0 ; i < n; i++) {
        cin >> op >> x;
        if (op == '+')
            punkty.insert(x);
        else
            punkty.erase(x);
        
        /*
        cout << "================\n";
        for (const auto &e : punkty)
            cout << e << ' ';
        cout << '\n';
        */

        if (punkty.size() < 3)
            cout << -1 << '\n';
        else {
            int wyn = max(*next(punkty.rbegin()) - *punkty.begin(), *punkty.rbegin() - *next(punkty.begin()));
            cout << wyn << '\n';
        }
    }

    return 0;
}
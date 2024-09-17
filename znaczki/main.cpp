#include <iostream>
#include <set>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;
    set<int> set1;
    set<int> set2;

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        set1.insert(k);
    }

    for (int i = 0; i < m; i++) {
        int k;
        cin >> k;
        set2.insert(k);
    }

    int wyn = 0;
    for (int zna : set2) {
        if (set1.count(zna) == 0) {
            wyn++;
        }
    }

    cout << wyn;

    return 0;
}

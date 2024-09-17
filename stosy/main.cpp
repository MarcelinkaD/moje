#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> l;

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        l.push_back(k);
    }

    vector<int> od_lewej_strony(n, 0);
    vector<int> od_prawej_strony(n, 0);

    od_lewej_strony[0] = l[0];
    for (int i = 1; i < n; i++) {
        od_lewej_strony[i] = (l[i] + od_lewej_strony[i - 1] / 2);
    }

    od_prawej_strony[n - 1] = l[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        od_prawej_strony[i] = (l[i] + od_prawej_strony[i + 1] / 2);
    }

    long long max_wyn = -1;
    for (int i = 0; i < n; i++) {
        long long wyn = l[i];

        if (i > 0) {
            wyn += od_lewej_strony[i - 1] / 2;
        }

        if (i < n - 1) {
            wyn += od_prawej_strony[i + 1] / 2;
        }

        max_wyn = max(max_wyn, wyn);
    }

    cout << max_wyn;

    return 0;
}

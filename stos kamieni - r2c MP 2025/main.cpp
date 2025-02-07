//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r2c/
#include <bits/stdc++.h>
using namespace std;

vector<int> l;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        l.push_back(x);
    }

    sort(l.begin(), l.end());
    int max_wyn = -1;
    int akt_wyn = 1;
    for (int i = 1; i < n ; i++) {
        if (l[i] == l[i - 1]) continue;
        if (l[i] - 1 == l[i - 1]) {
            akt_wyn++;
        } else {
            max_wyn = max(max_wyn, akt_wyn);
            akt_wyn = 1;
        }
    }
    max_wyn = max(max_wyn, akt_wyn);

    cout << max_wyn << endl;

    return 0;
}

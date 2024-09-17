#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    vector<int> kierunki;

    for (int i = 0; i < n; i++) {
        int rzad;
        cin >> rzad;
        kierunki.push_back(rzad);
    }

    int maxi, mini;
    maxi = -1;
    mini = n + 1;

    for (int i = 0; i < n; i++) {
        int zwrot;
        cin >> zwrot;

        if (zwrot == 1) {
            maxi = max(maxi, kierunki[i]);
        } else {
            mini = min(mini, kierunki[i]);
        }
    }

    if (maxi <= mini) {
        cout << "TAK";
    } else {
        cout << "NIE";
    }

    return 0;
}

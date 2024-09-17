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
    long long akt_sum = 0;
    vector<long long> sumy;
    sumy.push_back(0);

    for (int i = 0; i < n; i++) {
        long long kaw;
        cin >> kaw;
        akt_sum += kaw;
        sumy.push_back(akt_sum);
    }

    int q;
    cin >> q;

    for (int k = 0; k < q; k++) {
        int pocz, kon;
        cin >> pocz >> kon;
        cout << sumy[kon] - sumy[pocz - 1] << endl;
    }

    return 0;
}

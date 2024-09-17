#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    vector<vector<int>> graf;
    int n, k;
    cin >> n >> k;

    graf.resize(n + 1);
    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
    }

    for (int i = 1; i < n + 1; i++) {
        if (graf[i].size() >= 3) {
            cout << "w" << i << ": ";
            sort (graf[i].begin(), graf[i].end());
            for (int k = 0; k < graf[i].size(); k++) {
                cout << graf[i][k] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}

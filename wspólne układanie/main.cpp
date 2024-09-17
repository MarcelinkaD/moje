#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;
    vector <int>lit1(26, 0);
    vector <int>lit2(26, 0);

    for (int i = 0; i < n; i++) {
        char znak;
        cin >> znak;
        lit1[znak - 97]++;
    }

    for (int i = 0; i < m; i++) {
        char znak;
        cin >> znak;
        lit2[znak - 97]++;
    }

    int wyn = 0;

    for (int i = 0; i < 26; i++){
        wyn += min(lit1[i], lit2[i]);
    }

    cout << wyn;

    return 0;
}

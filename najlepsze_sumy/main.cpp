//https://szkopul.edu.pl/c/map-2024_2025/p/najs/
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    vector<int> l;
    int x;
    while (1) {
        cin >> x;
        if (x != 0) {
            l.push_back(x);
        } else {
            break;
        }
    }

    int n = l.size();
    int naj_wyn = -1e18;
    int akt_sum = 0;
    for (int i = 0; i < n; i++){
        akt_sum += l[i];
        if (akt_sum < l[i]) {
            akt_sum = l[i];
        }
        naj_wyn = max(akt_sum, naj_wyn);
    }

    cout << naj_wyn << endl;

    return 0;
}

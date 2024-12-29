//https://szkopul.edu.pl/c/map-2024_2025/p/tmp/
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

    int l[n];
    for (int i = 0; i < n; i++) {
        cin >> l[i];
    }

    int co;
    cin >> co;

    vector<int> wyn;
    for (int i = 0; i < n; i++) {
        if (l[i] == co) {
            wyn.push_back(i + 1);
        }
    }

    cout << wyn.size() << ' ';

    for (int i = 0; i < wyn.size(); i++) {
        cout << wyn[i] << ' ';
    }

    return 0;
}

//https://szkopul.edu.pl/c/map-2024_2025/p/cia/25253/
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    int akt_w = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        akt_w += x;
        cout << akt_w << ' ';
    }

    return 0;
}

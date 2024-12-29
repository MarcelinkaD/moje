//https://szkopul.edu.pl/c/map-2024_2025/p/szu/22143/
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
    int szuflady[n];

    for (int i = 0; i < n; i++){
        cin >> szuflady[i];
    }

    int w = 0;
    for (int i = n - 1; i > 0; i--){
        if (szuflady[i] < szuflady[i - 1]) {
            szuflady[i - 1] = szuflady[i] - 1;
            w++;
            if (szuflady[i - 1] <= 0) {
                cout << -1 << endl;
                return 0;
            }
        }
    }
    cout << w << endl;

    return 0;
}

#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        int n;
        cin >> n;

        int g = 0;
        int wyn = 0;
        for (int k = 0; k < n; k++) {
            int licz;
            cin >> licz;
            g += licz;

            if (g < 0) {
                wyn++;
                g = 0;
            }
        }

        cout << abs(g) + wyn << endl;
    }


    return 0;
}

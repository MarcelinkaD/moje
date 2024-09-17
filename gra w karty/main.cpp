#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    char war_m, kol_m;
    cin >> war_m >> kol_m;

    int q;
    cin >> q;

    for (int i = 0; i < q; i++){
        char war_s, kol_s;
        cin >> war_s >> kol_s;

        if (war_m == war_s) {
            cout << '1';
        } else {
            cout << '0';
        }

        if (kol_m == kol_s) {
            cout << '1';
        } else {
            cout << '0';
        }

        cout << endl;

    }

    return 0;
}

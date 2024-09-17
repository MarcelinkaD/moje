#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int wynik_ind = -1;
    float wynik_war = 10000.0;
    int n;
    cin >> n;
    int w_arr[n];

    for (int i = 0; i < n; i++) {
        int w;
        cin >> w;
        w_arr[i] = w;
    }

    for (int i = 0; i < n; i++) {
        float c;
        cin >> c;
        float opl = w_arr[i] / c;

        if (opl < wynik_war) {
            wynik_war = opl;
            wynik_ind = i + 1;
        }
    }

    cout << wynik_ind;
    return 0;
}

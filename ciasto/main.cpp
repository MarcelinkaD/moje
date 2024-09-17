#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int masa, v, czas;
    cin >> masa >> v >> czas;
    int ile_zje = v * czas;

    if (ile_zje >= masa) {
        cout << "TAK" << endl;
        cout << ile_zje - masa;
    } else {
        cout << "NIE" << endl;
        int w = v;
        while (w * czas <= masa) {
            w += 1;
        }
        cout << w << endl;
    }

    return 0;
}

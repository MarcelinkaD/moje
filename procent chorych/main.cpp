#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    long long Pa, Pb, Pba;
    cin >> Pa >> Pb >> Pba;

    /**
    Pa = Pa / 100.0;
    Pb = Pb / 100.0;
    Pba = Pba / 100.0;
    **/

    long long wynik = (Pba * Pa) / Pb;

    cout << (wynik) << '%';


    return 0;
}

//https://szkopul.edu.pl/c/map-2024_2025/p/sto1/
#include <iostream>
using namespace std;

#define ll long long

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    15 18 4
    ll a, b, k;
    cin >> a >> b >> k;

    if (b > a) {
        ll temp = a;
        a = b;
        b = temp;
    }

    /*if (k > a) {
        cout << 0 << endl;
        return 0;
    }
    */

    ll ile_a = a / k;
    ll ile_b = b / k;

    if (k * 2 <= b){
        cout << ((ile_a * 2) + (ile_b * 2) - 4) << endl;
    } else if (k <= b) {
        cout << ile_a << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}

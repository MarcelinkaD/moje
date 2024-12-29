//https://sio2.mimuw.edu.pl/c/oi32-1/p/usu/
#include <iostream>
using namespace std;

long long n, p, razem, pol, w;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    long long a, b;
    cin >> a >> b;

    razem = b - a + 1;
    pol = razem / 2;
    bool czy_a_nie_parz = a % 2;
    bool czy_b_nie_parz = b % 2;

    if (czy_a_nie_parz) {
        if (czy_b_nie_parz) {
            p = pol;
            n = razem - p;
        } else {
            p = pol;
            n = pol;
        }
    } else {
        if (czy_b_nie_parz) {
            p = pol;
            n = pol;
        } else {
            p = pol;
            n = razem - p;
        }
    }

    cout << razem -((n % 2) + (p % 2)) << endl;

    return 0;
}

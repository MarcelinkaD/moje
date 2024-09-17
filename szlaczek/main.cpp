#include <iostream>

using namespace std;

int main()
{
    long long n;
    long long a;
    long long b;
    cin >> n >> a >> b;

    if (a + b == 0 || a == 0) {
        cout << 0;
        return 0;
    }

    if (b == 0) {
        cout << n;
        return 0;
    }

    long long sab = a + b;
    long long ile_sab_w_n = n / sab;

    if (ile_sab_w_n * sab == n) {
        cout << ile_sab_w_n * a;
    } else {
        if (n - (ile_sab_w_n * sab) >= a){
            cout << (ile_sab_w_n * a) + a;
        } else {
            cout << (ile_sab_w_n * a) + n - (ile_sab_w_n * sab);
        }
    }


    return 0;
}

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int q;
    cin >> q;
    for (int i = 0; i < q; i++){
        int n;
        cin >> n;

        if (n == 1) {
            cout << 1;
        }

        for (int k = 1; k < n; k++) {
            if (__gcd(k, n) == 1) {
                cout << k << ' ';
            }
        }
        cout << endl;


    }

    return 0;
}

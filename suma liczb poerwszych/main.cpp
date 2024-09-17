#include <iostream>
#include <math.h>
using namespace std;

bool czy_pie(int x) {
    if (x == 0 || x == 1) {
        return 0;
    } else if (x == 2 || x == 3) {
        return 1;
    } else {
        int pier = sqrt(x);
        for (int i = 2; i <= pier; i++) {
            if (x % i == 0) {
                return 0;
            }
        }
        return 1;
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    long long n;
    cin >> n;

    while (n != 0) {
        if (n % 2 == 0) {
            cout << 'T' << endl;
        } else {
            if (czy_pie(n - 2)) {
                cout << 'T' << endl;
            } else {
                cout << 'N' << endl;
            }
        }
        cin >> n;

    }

    return 0;
}


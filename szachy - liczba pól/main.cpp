#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int pol;
    pol = (n * n) / 2;

    if (n % 2 == 0) {
        cout << pol << endl;
        cout << pol << endl;
    } else {
        cout << pol << endl;
        cout << pol + 1 << endl;
    }

    return 0;
}

// 1) Obwód (str. 56)
#include <iostream>
using namespace std;


int main()
{
    int n;
    cin >> n;
    int min_obw = (n + 1) * 2;

    for (int i = 2; i < n / 2; i++) {
        if (n % i == 0) {
            int a, b;
            a = i;
            b = n / i;
            min_obw = min(min_obw, (a + b) * 2);
        }
    }

    cout << min_obw << endl;

    return 0;
}





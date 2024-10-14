//https://szkopul.edu.pl/problemset/problem/wzEgXE9QizulWQd-HtbMhs8R/site/?key=statement
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    double r;
    cin >> r;

    if (r == 0) {
        cout << 0 << endl;
        cout << 0 << endl;
    } else {
        double pole = round((M_PI * (r * r)) * 1000.0) / 1000.0;
        double obwod = round((2 * r * M_PI) * 1000.0) / 1000.0;

        cout << fixed;
        cout << setprecision(3);
        cout << pole << endl;
        cout << obwod << endl;
    }

    return 0;
}

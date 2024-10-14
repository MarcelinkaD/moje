//https://szkopul.edu.pl/problemset/problem/2sZtw1mFxZd3Iwo6wZWStnzQ/site/?key=statement
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    double n;
    cin >> n;
    double cel = (5 * (n - 32.0)) / 9;

    cout << fixed;
    cout << setprecision(2);
    cout << round(cel * 100) / 100 << endl;

    return 0;
}

//https://szkopul.edu.pl/c/map-2024_2025/p/tro1/25405/
#include <iostream>
using namespace std;

int main()
{
    long long a, b, c;
    cin >> a >> b >> c;

    if (a + b > c && a + c > b && b + c > a) {
        cout << "TAK" << endl;
    } else {
        cout << "NIE" << endl;
    }

    return 0;
}

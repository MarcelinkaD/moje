//https://szkopul.edu.pl/c/map-2024_2025/p/ilit/
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    long long n;
    cin >> n;

    while (n > 0) {
        if (n % 16 >= 10) {
            cout << "TAK" << endl;
            return 0;
        }
        n /= 16;
    }

    cout << "NIE" << endl;
    return 0;
}

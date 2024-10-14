//https://szkopul.edu.pl/c/map-2024_2025/p/cwi/
#include <iostream>
using namespace std;

int main()
{
    int x, y;
    cin >> x >> y;

    if (x == 0) {
        if (y == 0) {
            cout << 0;
        } else {
            cout << "OY";
        }
    } else {
        if (y == 0) {
            cout << "OX";
        } else {
            if (x < 0) {
                if (y < 0) {
                    cout << "III";
                } else {
                    cout << "II";
                }
            } else {
                if (y < 0) {
                    cout << "IV";
                } else {
                    cout << "I";
                }
            }
        }
    }

    return 0;
}

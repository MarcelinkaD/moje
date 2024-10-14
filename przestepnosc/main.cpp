//https://szkopul.edu.pl/c/map-2024_2025/p/prz/25251/
#include <iostream>
using namespace std;

int main()
{
    int r;
    cin >> r;

    if (r % 4 == 0) {
        if (r % 100 == 0 && r % 400 != 0) {
            cout << "NIE" << endl;
        } else {
            cout << "TAK" << endl;
        }
    } else {
        cout << "NIE" << endl;
    }

    return 0;
}

//https://szkopul.edu.pl/c/map-2024_2025/p/sza/
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++){
        if (i % 2 == 1) {
            for (int k = 1; k <= n; k++) {
                if (k % 2 == 1) {
                    cout << '0';
                } else {
                    cout << '1';
                }
            }
        } else {
            for (int k = 1; k <= n; k++) {
                if (k % 2 == 1) {
                    cout << '1';
                } else {
                    cout << '0';
                }
            }
        }
        cout << endl;
    }

    return 0;
}

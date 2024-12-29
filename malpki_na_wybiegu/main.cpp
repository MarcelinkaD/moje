//https://szkopul.edu.pl/c/map-2024_2025/p/mnw/
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n + 2; i++) {
        cout << '#';
    }
    cout << endl;

    cout << '#';
    for (int i = 0; i < n; i++) {
        cout << '@';
    }
    cout << '#';
    cout << endl;

    for (int i = 0; i < n + 2; i++) {
        cout << '#';
    }

    return 0;
}

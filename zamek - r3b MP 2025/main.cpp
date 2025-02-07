//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r3b/
#include <iostream>
using namespace std;

int main()
{
    int ile = 0;
    for (int i = 0; i < 10; i++) {
        char x;
        cin >> x;
        if (x == '?') {
            ile++;
        }
    }

    cout << (ile * ile * ile * ile) << endl;

    return 0;
}

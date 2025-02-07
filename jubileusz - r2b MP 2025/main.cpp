//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r2b/
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    long long n;
    cin >> n;
    long long akt_pot = 1;
    while (akt_pot < n) {
        akt_pot *= 2;
    }
    cout << akt_pot - n << endl;
    return 0;
}

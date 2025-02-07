//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r2a/
#include <iostream>
#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll a, b;
    cin >> a >> b;
    ll w;
    cin >> w;

    if (a * b == w) {
        cout << "DOBRZE" << endl;
    } else {
        cout << "TYLKO SZYBKO" << endl;
    }

    return 0;
}

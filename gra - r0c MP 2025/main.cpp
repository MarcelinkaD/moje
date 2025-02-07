//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r0c/
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cout << 9 - x << endl;
    }

    return 0;
}

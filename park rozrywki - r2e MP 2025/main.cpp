//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r2e/
#include <iostream>
using namespace std;

const int MAXN = 105;
int wyn[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++){
        cout << "1 " << i << endl;
        cin >> wyn[i];
    }

    cout << '3';
    for (int i = 1; i <= n; i++) {
        cout << ' ' << wyn[i];
    }
    cout << endl;
    return 0;
}

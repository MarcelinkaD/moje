//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r4b/
#include <iostream>
using namespace std;

const int MAXN = 1000005;
int wyn[MAXN];

int main()
{
    int n;
    cin >> n;
    wyn[1] = 1;
    wyn[2] = 1;

    for (int i = 3; i <= n; i++) {
        wyn[i] = wyn[i - wyn[i - 1]] + wyn[i - wyn[i - 2]];
    }

    cout << wyn[n] << endl;
    return 0;
}

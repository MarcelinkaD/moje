//https://szkopul.edu.pl/c/map-2024_2025/p/sre/25361/
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    int sumy[n + 1];

    for (int i = 1; i <= n; i++){
        int x;
        cin >> x;
        sumy[i] = sumy[i - 1] + x;
    }

    int a, b;
    cin >> a >> b;

    int w = (sumy[b] - sumy[a - 1]) / (b - a + 1);
    cout << w;

    return 0;
}

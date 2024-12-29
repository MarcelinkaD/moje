//https://szkopul.edu.pl/c/map-2024_2025/p/abs/25243/
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    int maxx = -500005;
    int minn = 500005;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        maxx = max(maxx, x);
        minn = min(minn, x);
    }

    cout << maxx - minn;

    return 0;
}

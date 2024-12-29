//https://szkopul.edu.pl/c/map-2024_2025/p/prs/25298/#
#include <iostream>
using namespace std;

const int MAXN = 1000005;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    pair<long long, long long> lewo;
    pair<long long, long long> prawo;

    lewo.first = MAXN;
    lewo.second = MAXN;
    prawo.first = MAXN * -1;
    prawo.second = MAXN * -1;

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;

        if (x < lewo.first) {
            lewo.first = x;
        }

        if (y < lewo.second) {
            lewo.second = y;
        }

        if (x > prawo.first) {
            prawo.first = x;
        }

        if (y > prawo.second) {
            prawo.second = y;
        }

    }

    long long a = prawo.first - lewo.first;
    long long b = prawo.second - lewo.second;
    cout << (a * 2) + (b * 2) << endl;


    return 0;
}

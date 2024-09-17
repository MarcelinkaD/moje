#include <iostream>

using namespace std;

long long suma_kont(long long n) {
    long long w = 0;
    int waga = 1;
    while (n > 0) {
        w += (n % 10) * waga;
        waga += 1;
        n /= 10;
    }

    return w;

}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    long long a, b;
    cin >> a >> b;
    cout << suma_kont(a) << " " << suma_kont(b);
    return 0;
}

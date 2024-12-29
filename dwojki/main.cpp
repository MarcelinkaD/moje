//https://szkopul.edu.pl/c/map-2024_2025/p/dwo/
#include <iostream>
using namespace std;

#define ll long long

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie();
    cout.tie();

    ll n;
    cin >> n;

    ll pot_dwojki = 1; // inaczej 2 do 0
    int wyn = 0;

    while (pot_dwojki <= n) {
        wyn++;
        pot_dwojki *= 2;
    }

    cout << wyn << endl;
    return 0;
}

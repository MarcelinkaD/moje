#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int wyn = 0;
    for (int i = 0; i < 5; i++){
        int a, b;
        cin >> a >> b;
        wyn += (a * b);
    }
    cout << wyn << '\n';

    return 0;
}

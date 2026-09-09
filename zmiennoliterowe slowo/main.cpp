#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    char pop, akt;
    cin >> pop;
    int wyn = 0;
    while (cin >> akt){
        if (pop == akt) {
            wyn++;
        }
        pop = akt;
    }
    cout << wyn << '\n';

    return 0;
}

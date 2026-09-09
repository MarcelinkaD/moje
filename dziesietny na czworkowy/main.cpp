#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> wyn;
    while (n){
        int reszta = n % 4;
        wyn.push_back(reszta);
        n /= 4;
    }

    reverse(wyn.begin(), wyn.end());
    for (auto i : wyn){
        cout << i;
    }

    return 0;
}

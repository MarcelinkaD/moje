#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    vector<int> l;

    for (int i = 0; i < n; i++) {
        int kan;
        cin >> kan;
        l.push_back(kan);
    }

    sort(l.begin(), l.end(), greater<int>());

    for (int i = 0; i < 10; i++) {
        cout << l[i] << ' ';
    }

    return 0;
}

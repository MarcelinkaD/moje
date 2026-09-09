#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> wyn;

int main()
{
    for (int i = 0; i < 4; i++){
        int a, b;
        cin >> a >> b;
        wyn.push_back({-a, -b});
    }

    sort(wyn.begin(), wyn.end());

    for (auto p : wyn){
        cout << -p[0] << ' ' << -p[1] << endl;
    }

    return 0;
}

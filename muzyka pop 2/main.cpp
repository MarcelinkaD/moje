#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 5;

int ile_bit(int x){
    return __builtin_popcount(x);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> wyn;
    vector<int> ile(MAXN);

    ile[0] = 0;
    int ind = 0;
    for (int i = 1; i < MAXN; i++){
        int bity = ile_bit(i);
        ile[i] = ile[i - 1] + bity;
        if (ile[i] >= n){
            ind = i;
            break;
        }
    }

    int ile_wyk = 0;
    while (ile_wyk < n){
        if (ile[ind] >= n - ile_wyk){
            ile_wyk += ile[ind] - ile[ind - 1];
            wyn.push_back(ind);
        }
        ind--;
    }

    cout << wyn.size() << '\n';
    for (auto i : wyn){
        cout << i << ' ';
    }

    return 0;
}

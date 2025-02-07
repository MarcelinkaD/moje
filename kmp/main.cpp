//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/kmp1/
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e7 + 5;
int ps[MAXN];
vector<char> s;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    s.push_back('?');
    for (int i = 0; i < n; i++){
        char x;
        cin >> x;
        s.push_back(x);
    }

    ps[0] = -1;
    int t = -1;
    for (int i = 1; i <= n; i++){
        while (t >= 0 && s[t + 1] != s[i]){
            t = ps[t];
        }
        t++;
        ps[i] = t;
    }

    for (int i = 1; i <= n; i++){
        cout << ps[i] << ' ';
    }

    return 0;
}

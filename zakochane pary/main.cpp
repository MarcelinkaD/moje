#include <iostream>
#include <map>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m, s;
    cin >> n >> m >> s;
    map<int, int> ch;
    long long w = 0;

    for (int i = 0; i < n; i++){
        int y;
        cin >> y;
        ch[y]++;
    }

    for (int k = 0; k < m; k++){
        int x;
        cin >> x;

        if (ch.find(s - x) != ch.end()) {
            w += ch[s - x];
        }
    }

    cout << w << endl;

    return 0;
}

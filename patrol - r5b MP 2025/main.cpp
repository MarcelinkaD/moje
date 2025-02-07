//https://szkopul.edu.pl/c/mistrz-programowania-2025/p/r5b/
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string s;
    cin >> s;

    int dlu = s.size();
    if (dlu == 1) {
        cout << s << endl;
        return 0;
    }

    bool czy_przerw = false;
    int zacz = s[0] - '0';
    for (int i = 1; i < dlu; i++){
        int x = s[i] - '0';
        int pop = s[i - 1] - '0';
        if (x > zacz) {
            zacz++;
            break;
        } else if (x < zacz) {
            break;
        }
    }

    if (zacz == 10) {
        zacz = 1;
        dlu++;
    }

    for (int i = 0; i < dlu; i++){
        cout << zacz;
    }

    return 0;

}

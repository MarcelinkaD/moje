//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/cyk1/
#include <bits/stdc++.h>
using namespace std;

vector<int> KMP(const string& str) {
    int m = str.size();
    vector<int> ps(m);
    ps[0] = 0;
    for (int i = 1; i < m; i++) {
        int j = ps[i - 1];
        while (j > 0 && str[i] != str[j])
            j = ps[j - 1];
        if (str[i] == str[j])
            j++;
        ps[i] = j;
    }
    return ps;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    string s1, s2;
    cin >> s1 >> s2;

    vector<int> ps = KMP(s1);

    int j = 0;
    for (int i = 0; i < 2 * n; i++) {
        while (j > 0 && s2[i % n] != s1[j])
            j = ps[j - 1];
        if (s2[i % n] == s1[j])
            j++;
        if (j == n) {
            cout << "TAK" << endl;
            return 0;
        }
    }

    cout << "NIE" << endl;
    return 0;
}

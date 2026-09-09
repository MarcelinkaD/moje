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

    int n, m;
    cin >> n >> m;
    string s1, s2;
    cin >> s1 >> s2;

    vector<int> ps = KMP(s2);

    int wyn = 0;
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j > 0 && s1[i] != s2[j])
            j = ps[j - 1];
            if (s1[i] == s2[j])
                j++;
            if (j == m) {
                wyn++;
                j = ps[j - 1];
            }
    }

    cout << wyn << endl;
    return 0;
}

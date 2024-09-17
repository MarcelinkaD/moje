/*
#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n, w, MAXN;
    w = -1;
    cin >> n;
    map<int, int> zlicz;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        zlicz[x]++;
        MAXN = max(MAXN, x);
    }

    for (int i = 1; i <= MAXN; i++) {
        if (zlicz.find(i) != zlicz.end() && zlicz.find(i + 1) != zlicz.end()) {
            w = max(w, zlicz[i] + zlicz[i + 1]);
        }
    }
    cout << w << endl;
    return 0;
}
*/

#include <string>
#include <iostream>
#include <stack>
using namespace std;

int main()
{
    int q;
    cin >> q;

    for (int k = 0; k < q; k++){
        string s;
        cin >> s;
        stack<char> stos;
        string wyn = "TAK";

        for (int i = 0; i < s.size(); i++){
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                stos.push(s[i]);
            } else {
                if (!stos.empty()) {
                    int x = stos.top();
                    if (x == '(' && s[i] == ')') {
                        stos.pop();
                    } else if (x == '{' && s[i] == '}') {
                        stos.pop();
                    } else if (x == '[' && s[i] == ']') {
                        stos.pop();
                    } else {
                        wyn = "NIE";
                    }
                } else {
                    wyn = "NIE";
                }
            }
        }

        if (!stos.empty()) {
            wyn = "NIE";
        }

        cout << wyn << endl;
    }

    return 0;
}


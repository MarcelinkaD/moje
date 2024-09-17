#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int q;
    cin >> q;
    for (int k = 0; k < q; k++) {
        string s;
        string w;
        w = "TRUE";
        cin >> s;
        stack<int> stos;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stos.push('(');
            } else if (s[i] == ')') {
                if (!stos.empty() && stos.top() == '(') {
                    stos.pop();
                } else {
                    w = "FALSE";
                    break;
                }
            } else {
                w = "FALSE";
                break;
            }
        }
        if (!stos.empty()) {
            w = "FALSE";
        }

        cout << w << endl;
    }

    return 0;
}

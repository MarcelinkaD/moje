#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
    int q;
    cin >> q;

    for (int i = 0; i < q; i++) {
        stack<char> stos;
        string s;
        cin >> s;
        string wyn = "TAK";

        for (int k = 0; k < s.size(); k++) {
            char akt_naw;
            akt_naw = s[k];

            if (akt_naw == '[' || akt_naw == '{' || akt_naw == '(') {
                stos.push(akt_naw);
            } else {
                if (stos.size() == 0) {
                    wyn = "NIE";
                    break;
                }
                char ost = stos.top();
                if (akt_naw == ']' && ost != '[') {
                    wyn = "NIE";
                    break;
                } else if (akt_naw == '}' && ost != '{') {
                    wyn = "NIE";
                    break;
                } else if (akt_naw == ')' && ost != '(') {
                    wyn = "NIE";
                    break;
                } else {
                    stos.pop();
                }
            }
        }

        if (wyn == "TAK") {
            if (!stos.empty()) {
                wyn = "NIE";
            }
        }
        cout << wyn << endl;
    }



    return 0;
}

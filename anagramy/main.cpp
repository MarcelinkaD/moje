#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string s1, s2;
    cin >> s1;
    cin >> s2;
    map<char, int> c1;
    map<char, int> c2;

    if (s1.size() == s2.size()) {
        for (int i = 0; i < s1.size(); i++){
            c1[s1[i]]++;
            c2[s2[i]]++;
        }

        for (int k = 0; k < s1.size(); k++){
            if (c1[s1[k]] != c2[s1[k]]) {
                cout << "NIE" << endl;
                return 0;
            }
        }

        cout << "TAK" << endl;
        return 0;

    } else {
        cout << "NIE" << endl;
        return 0;
    }

    return 0;
}

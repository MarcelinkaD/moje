/*
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    map<char, int> zlicz;
    string s;
    cin >> s;
    pair<char, int> max1;
    pair<char, int> max2;
    max1.second = -1;
    max2.second = -1;

    for (int i = 0; i < s.size(); i++){
        zlicz[s[i]]++;
        if (zlicz[s[i]] > max1.second) {
            max1.first = s[i];
            max1.second = zlicz[s[i]];
        } else if (zlicz[s[i]] > max2.second && s[i] != max1.first) {
            max2.first = s[i];
            max2.second = zlicz[s[i]];
        }
    }

    cout << max(max1.second, max2.second) << endl;
    return 0;
}
*/

#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;
    map<int, pair<int, int>> wyst;
    wyst[0].first = 0;
    int n = s.size();
    int sumy[n + 1];
    sumy[0] = 0;
    int wyn = -1;

    for (int i = 0; i < n; i++){
        if (s[i] == 'a') {
            sumy[i + 1] = sumy[i] + 1;
        } else {
            sumy[i + 1] = sumy[i] - 1;
        }

        int x = sumy[i + 1];
        if (wyst.find(x) != wyst.end()) {
            wyst[x].second = i + 1;
            wyn = max(wyn, wyst[x].second - wyst[x].first);
        } else {
            wyst[x].first = i + 1;
        }

    }
    cout << wyn << endl;
}

#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    map<int, int> art;
    vector<int> kol;

    for (int i = 0; i < n; i++) {
        int a, s;
        cin >> a >> s;

        if (art.find(a) != art.end()) {
            art[a] += s;
        } else {
            art[a] = 0;
            art[a] += s;
            kol.push_back(a);
        }
    }

    cout << art.size() << endl;

    for (int i = 0; i < kol.size(); i++) {
        cout << kol[i] << ' '<< art[kol[i]] << endl;
    }

    return 0;
}

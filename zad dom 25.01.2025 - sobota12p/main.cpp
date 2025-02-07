//https://codeforces.com/problemset/problem/1045/I (brut)
/*#include <bits/stdc++.h>
using namespace std;

vector<int> napisy;
int ile[26];

int ile_jedynek(int maska) {
    int w = 0;
    for (int bit = 0; bit < 26; bit++) {
        if ((maska >> bit) & 1){
            w++;
        }
    }
    return w;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    for (int i = 0; i < 26; i++) ile[i] = i;

    int n;
    cin >> n;
    int wyn = 0;
    int ile0 = 0;
    int ile1 = 0;

    for (int k = 0; k < n; k++){
        string x;
        cin >> x;
        int maska = 0;
        for (int i = 0; i < x.size(); i++){
            char lit = x[i];
            int bit = ile[lit - 'a'];
            maska ^= (1 << bit);
        }
        if (maska == 0) {
            wyn += ile0;
            wyn += ile1;
            ile0++;
        } else if (ile_jedynek(maska) == 1) {
            wyn += ile0;
            ile1++;
            napisy.push_back(maska);
        } else {
            napisy.push_back(maska);
        }
    }

    for (int i = 0; i < napisy.size(); i++){
        int m1 = napisy[i];
        for (int k = i + 1; k < napisy.size(); k++) {
            int m2 = napisy[k];
            int ile_jed = ile_jedynek((m1 ^ m2));
            if (ile_jed == 0 || ile_jed == 1){
                wyn++;
            }
        }
    }
    cout << wyn << endl;
    return 0;
}
*/

//https://codeforces.com/problemset/problem/1045/I (fast)
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

unordered_map<ll, ll> maski;
int ile[26];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    for (int i = 0; i < 26; i++) ile[i] = i;

    int n;
    cin >> n;
    ll wyn = 0;

    for (int k = 0; k < n; k++){
        string x;
        cin >> x;
        ll maska = 0;
        for (int i = 0; i < x.size(); i++){
            char lit = x[i];
            int bit = ile[lit - 'a'];
            maska ^= (1 << bit);
        }
        wyn += maski[maska];
        for (int i = 0; i < 26; i++){
            maska ^= (1 << i);
            wyn += maski[maska];
            maska ^= (1 << i);
        }
        maski[maska]++;
    }

    cout << wyn << endl;
    return 0;
}

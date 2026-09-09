#include <bits/stdc++.h>
using namespace std;

stack<char> stos;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    string s;
    cin >> s;

    int i = 0;
    int w = 0;
    while (true){
        if (stos.size() >= 2) {
            char pop1 = stos.top();
            stos.pop();
            char pop2 = stos.top();
            stos.pop();
            if (pop1 == pop2){
                w += 2;
            } else {
                stos.push(pop2);
                stos.push(pop1);
                if (i == n){
                    break;
                }
            }
        }
        if (i < n){
            char akt_znak = s[i];
            stos.push(akt_znak);
            i++;
        }
        if (i == n && stos.size() < 2){
            break;
        }
    }

    cout << w << endl;

    return 0;
}

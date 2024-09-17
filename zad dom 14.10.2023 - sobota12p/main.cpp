// 3) https://szkopul.edu.pl/problemset/problem/KlznBqTfieN-sWvUfTD0BJdT/site/?key=statement

#include <iostream>
#include <string>
using namespace std;

const int MAXN = 1000007;

int main()
{
    int n, h, akt_h, w;
    string s;
    cin >> n >> h;
    cin >> s;
    akt_h = 0;
    w = 0;

    for (int i = 0; i < n; i++){
        char akt_s = s[i];
        if (akt_s == '(' && akt_h == h){
            akt_s = ')';
            w++;
        } else if (akt_s == ')' && akt_h == 0) {
            akt_s = '(';
            w++;
        }

        if (akt_s == '(') {
            akt_h++;
        } else {
            akt_h--;
        }
    }

    cout << w << endl;

    return 0;
}

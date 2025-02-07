//https://szkopul.edu.pl/c/map-2024_2025/p/pdw/
#include <bits/stdc++.h>
using namespace std;

string potegi[105];

string nast(string n) {
    int x = 0;
    char znak;
    for (int i = 0; i < n.size(); i++){
        x = (n[i] + n[i] - '0' - '0') + x;
        znak = (x % 10) + '0';
        x /= 10;
        n[i] = znak;
    }
    if (x) {
        n = n + '1';
    }
    return n;
}

bool sprawdz(string s1, string s2) {
    if (s1.size() * 2 >= s2.size()){
        return 0;
    }
    for (int i = 0; i < s1.size(); i++){
        if (s1[i] != s2[i]){
            return 0;
        }
    }
    return 1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string n;
    cin >> n;

    potegi[0] = "1";
    for (int i = 1; i <= 100; i++){
        potegi[i] = nast(potegi[i - 1]);
    }

    for (int i = 1; i <= 100; i++){
        reverse(potegi[i].begin(), potegi[i].end());
    }

    for (int i = 6; i <= 100; i++){
        if (sprawdz(n, potegi[i])) {
            cout << i << endl;
            return 0;
        }
    }

    return 0;
}

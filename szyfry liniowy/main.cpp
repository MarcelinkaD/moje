#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int a, b;
    cin >> a >> b;
    vector <char>literki = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    string ciag;
    cin >> ciag;

    for (int i = 0; i < ciag.size(); i++) {
        char znak = ciag[i];
        int x = znak - 97;
        cout << literki[(a * x + b) % 26];
    }

    return 0;
}

//AleMozgi 2024/2025
#include <bits/stdc++.h>
using namespace std;

stack<int> stos;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;
    int n = s.size();

    for (int i = 0; i < n; i++){
        char znak = s[i];
        if (!stos.empty() && stos.top() == znak){
            stos.pop();
        } else {
            stos.push(znak);
        }
    }
    cout << stos.size() << endl;

    return 0;
}

//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/pla/30145/
#include <bits/stdc++.h>
using namespace std;

vector<int> wys;
stack<int> stos;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;
        wys.push_back(b);
    }

    int wyn = 0;
    for (int i = 0; i < n; i++){
        while (!stos.empty() && stos.top() > wys[i]){
            stos.pop();
        }
        if (stos.empty() || stos.top() < wys[i]) {
            stos.push(wys[i]);
            wyn++;
        }
    }
    cout << wyn << endl;

    return 0;
}

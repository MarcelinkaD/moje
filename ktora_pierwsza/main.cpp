//AleMozgi 2024/2025
#include <bits/stdc++.h>
using namespace std;

bool czy_pie(int x){
    if (x == 0 || x == 1){
        return 0;
    }
    int pierw = sqrt(x);
    for (int i = 2; i <= pierw; i++){
        if (x % i == 0){
            return 0;
        }
    }
    return 1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c;
    cin >> a >> b >> c;

    if (a % 2 == 0 && c % 2 == 0){
        cout << b << endl;
    } else {
        if (czy_pie(a)){
            cout << a << endl;
        } else {
            cout << c << endl;
        }
    }

    return 0;
}

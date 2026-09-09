#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    if (n == 1 || n == 2 || n == 4 || n == 5 || n == 7 || n == 10 || n == 13){
        cout << "NIE" << '\n';
    } else {
        cout << "TAK" << '\n';
    }

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

long long potega(long long a, long long b, long long mod){
    if (b == 0){
        return 1;
    }

    long long parz = potega(a, b / 2, mod) * potega(a, b / 2, mod);
    if (b % 2 == 0){
        return (parz) % mod;
    } else {
        return (a * parz) % mod;
    }
}

int main()
{
    cout << potega(2, 30, 100) << endl;
    return 0;
}

// https://szkopul.edu.pl/problemset/problem/eSgi8Ae29vCPojodBrdDAooI/site/?key=statement
#include <iostream>
#include <string>
using namespace std;

int main()
{
    long long n, m, ile;
    cin >> n >> m;
    cin >> ile;

    if ((ile % n == 0 || ile % m == 0) && ile < n * m) {
        cout << "TAK" << endl;
    } else {
        cout << "NIE" << endl;
    }

    return 0;
}

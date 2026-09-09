// 2) gra z liczb¹
#include <iostream>
using namespace std;

int main()
{
    long long n;
    cin >> n;

    if (n % 2 == 0){
        cout << "Wygra pierwszy gracz" << endl;
    } else {
        cout << "Wygra drugi gracz" << endl;
    }

    return 0;
}

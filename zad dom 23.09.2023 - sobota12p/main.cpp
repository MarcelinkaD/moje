/*
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    int a_do_teraz = 0;
    int wyn = 0;

    for (int i = 0; i < n; i++){
        if (s[i] == 'A') {
            a_do_teraz++;
        } else {
            wyn += a_do_teraz;
        }
    }

    cout << wyn << endl;

    return 0;
}
*/

#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int przez10 = 0;
    int przez5 = 0;
    int przez2 = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        if (x % 10 == 0) {
            przez10++;
        } else if (x % 2 == 0) {
            przez2++;
        } else if (x % 5 == 0) {
            przez5++;
        }
    }

    int wynik = (przez10 * (n - 1)) + (przez2 * przez5);

    cout << wynik << endl;

    return 0;
}


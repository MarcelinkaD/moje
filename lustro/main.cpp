#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int jaka_potega = 1;
    int n;
    cin >> n;
    int w = 0;

    for (int do_ilu = 0; do_ilu <= 9; do_ilu++) {
        if (jaka_potega > n) {
            jaka_potega = jaka_potega / 10;
            break;
        } else {
            jaka_potega = jaka_potega * 10;
        }
    }

    while (n > 0) {
        int reszta;
        reszta = n % 10;

        if (reszta != 0) {
            w += reszta * jaka_potega;
        }

        jaka_potega /= 10;
        n /= 10;
    }

    cout << w;
    return 0;
}

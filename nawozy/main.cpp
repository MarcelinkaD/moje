#include <iostream>
#include <vector>
using namespace std;

int przelicz_na_licz(int n){
    return n - 48;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int licz_naw;
    int licz_miejsc;
    cin >> licz_naw >> licz_miejsc;
    int ile_dow_naw = 0;
    vector<int> ile_jak_pot(licz_naw + 1, 0);
    int ile_mamy_naw = 0;

    for (int i = 0; i < licz_miejsc; i++){
        char co_pot;
        cin >> co_pot;
        if (co_pot == 'D') {
            ile_dow_naw++;
        } else {
            int co_pot_int = co_pot;
            ile_jak_pot[przelicz_na_licz(co_pot_int)]++;
        }
    }

    for (int i = 0; i < licz_naw; i++){
        int ile_danego_naw;
        cin >> ile_danego_naw;
        ile_mamy_naw += ile_danego_naw;
        if (ile_jak_pot[i + 1] <= ile_danego_naw){
            ile_mamy_naw -= ile_jak_pot[i + 1];
        } else {
            cout << "NIE";
            return 0;
        }
    }

    if (ile_mamy_naw < ile_dow_naw) {
        cout << "NIE";
        return 0;
    } else {
        cout << "TAK";
        return 0;
    }

    return 0;
}

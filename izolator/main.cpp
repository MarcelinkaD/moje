//https://szkopul.edu.pl/c/oki-poziom-2-202425/p/izo/21767/
#include <bits/stdc++.h>
using namespace std;

vector<int> l;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    int wyn = 0;
    int suma = 0;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        suma += x;
        l.push_back(x);
    }

    sort(l.begin(), l.end());

    if (n % 2 == 0) {
        int pol = n / 2;
        for (int i = 0; i < pol; i++){
            wyn += l[i];
        }
        wyn *= -1;

        for (int i = pol; i < n; i++){
            wyn += l[i];
        }
        cout << wyn + suma << endl;

    } else {
        int pol = n / 2;
        for (int i = 0; i < pol; i++){
            wyn += l[i];
        }
        wyn *= -1;

        for (int i = pol + 1; i < n; i++){
            wyn += l[i];
        }

        cout << wyn + suma << endl;
    }

    return 0;
}

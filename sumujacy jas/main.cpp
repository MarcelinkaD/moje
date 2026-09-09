//https://szkopul.edu.pl/c/map-2024_2025/p/sum/18487/
#include <bits/stdc++.h>
using namespace std;

const int MAXM = 200 + 2;
char wyn[MAXM];
char akt_licz[MAXM];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int pol = 101;
    for (int i = 0; i < n; i++){
        string licz;
        cin >> licz;
        bool czy_plus = 1;

        if (licz[0] == '-'){
            czy_plus = 0;
            licz.erase(0, 1);
        } else if (licz[0] == '+'){
            licz.erase(0, 1);
        }



    }


}

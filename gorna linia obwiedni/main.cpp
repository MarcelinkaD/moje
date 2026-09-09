#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    pair<int, int> pop;
    cin >> pop.first >> pop.second;
    int pop_lezy = pop.second;
    int pop_stoi = pop.first;
    for (int i = 1; i < n; i++){
        pair<int, int> akt;
        cin >> akt.first >> akt.second;
        int lezy = max(pop_lezy + akt.second + abs(pop.first - akt.first), pop_stoi + akt.second + abs(pop.second - akt.first));
        int stoi = max(pop_lezy + akt.first + abs(pop.first - akt.second), pop_stoi + akt.first + abs(pop.second - akt.second));
        pop_lezy = lezy;
        pop_stoi = stoi;
        pop = akt;
    }

    cout << max(pop_lezy, pop_stoi) << '\n';

    return 0;
}

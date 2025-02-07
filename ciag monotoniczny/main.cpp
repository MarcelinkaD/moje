//https://szkopul.edu.pl/c/map-2024_2025/p/cmo/
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio();
    cin.tie(0);

    string x;
    cin >> x;
    int zlicz[26] = {};
    int m = 0;
    int maxi = -1;

    for (int i = 0; i < x.size(); i++){
        int znak = (int)x[i];
        zlicz[znak - 'a']++;
        maxi = max(zlicz[znak - 'a'], maxi);
    }

    for (int i = 0; i < x.size(); i++){
        int znak = (int)x[i];
        if (zlicz[znak - 'a'] == maxi){
            if (znak > m){
                m = znak;
            }
        }
    }

    for (int lit = (int)'a'; lit <= (int)'z'; lit++){
        if (lit != m){
            for (int i = 0; i < zlicz[lit - 'a']; i++){
                cout << char(lit);
            }
        }
    }

    return 0;
}

// 3) Implementacja wyszukiwania lidera w O(N)
/*
#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n;
    cin >> n;
    map<int, int> zlicz;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        zlicz[x]++;

        if(zlicz[x] > n / 2) {
            cout << x << endl;
            return 0 ;
        }
    }
    cout << "BRAK" << endl;
    return 0;
}


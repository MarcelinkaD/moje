#include <bits/stdc++.h>
using namespace std;

vector<int> doc_wyn = {1, 2, 3, 4, 5};
vector<int> wyn;

void wypisz(){
    for (auto s : wyn){
        cout << s << ' ';
    }
    cout << '\n';
}

int main()
{
    for (int i = 0; i < 5; i++){
        int x;
        cin >> x;
        wyn.push_back(x);
    }

    while (wyn != doc_wyn){
        for (int i = 0; i < 4; i++){
            if (wyn[i] > wyn[i + 1]){
                int temp = wyn[i];
                wyn[i] = wyn[i + 1];
                wyn[i + 1] = temp;
                wypisz();
            }
        }
    }

    return 0;
}

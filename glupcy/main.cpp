#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int zlacz(vector<int>& l, vector<int>& p){
    int i = 0, j = 0;
    int w = 0;
    sort(l.begin(), l.end());
    sort(p.begin(), p.end());
    while (i < l.size() && j < p.size()){
        if (l[i] <= p[j]){
            i++;
        } else {
            j++;
            w += l.size() - i;
        }
    }
    return w;
}

int zlicz_inw(vector<int>& t){
    if (t.size() <= 1){
        return 0;
    }

    int srodek = (int)t.size() / 2;
    vector<int> lewo;
    for (int i = 0; i < srodek; i++){
        lewo.push_back(t[i]);
    }
    vector<int> prawo;
    for (int i = srodek; i < t.size(); i++){
        prawo.push_back(t[i]);
    }

    int wyn = zlicz_inw(lewo) + zlicz_inw(prawo) + zlacz(lewo, prawo);
    return wyn;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> li(n);
    for (int i = 0; i < n; i++){
        cin >> li[i];
    }

    cout << zlicz_inw(li) << '\n';

    return 0;
}

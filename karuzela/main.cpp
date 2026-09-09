#include <bits/stdc++.h>
using namespace std;

double e = 2.718281828459;
double pi = 3.14159265358979323;
double l = -1;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie();

    string n;
    cin >> n;
    int N = 0;

    double wyn = 1;
    for (int k = 0; k < n.size(); k++){
        char i = n[k];
        if (i == '1'){
            wyn *= 1;
        } else if (i == '2'){
            wyn *= 2;
        } else if (i == '3'){
            wyn *= e;
        } else if (i == '4'){
            wyn *= pi;
        } else if (i == '5'){
            wyn *= 5;
        } else if (i == '6'){
            wyn *= 9;
        } else if (i == '7'){
            wyn *= l;
        } else if (i == '8'){
            wyn *= 8;
        } else if (i == '9'){
            wyn *= 6;
        } else if (i == '0'){
            wyn *= 0;
        }
        N += i - '0';
        if (k != n.size() - 1){
            N *= 10;
        }
    }

    cout << fixed << setprecision(12);
    cout << wyn + N << endl;

    return 0;
}

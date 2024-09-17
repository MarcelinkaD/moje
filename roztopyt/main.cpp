#include <iostream>
using namespace std;

int MAXN = 10;
long long grub_snie[10] = {0};

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        long long a, b;
        cin >> a >> b;
        grub_snie[a] += 1;
        grub_snie[b + 1] -= 1;
    }

    long long wyn = -1;

    for (int k = 1; k <= MAXN; k++) {
        grub_snie[k] = grub_snie[k - 1] + grub_snie[k];
        wyn = max(wyn, grub_snie[k]);
    }

    cout << wyn << endl;

    return 0;
}

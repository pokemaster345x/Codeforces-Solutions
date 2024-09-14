#include <bits/stdc++.h>
using namespace std;

int t, n, aux, cont1, cont2, aux3 = 0;

int main() {
    cin >> t;
    for (int i = 0; i < t; i++) {
        cont1 = cont2 = 0;
        cin >> n;
        vector<int> a(n);  
        cin >> a[0];
        aux = a[0];

        for (int x = 1; x < n; x++) { 
            cin >> a[x];
            if (a[x] == aux) {
                cont1++;
            } else {
                cont2++;
                aux3 = x + 1;
            }
        }
        
        if (cont1 < cont2) {
            cout << "1" << endl;
        } else {
            cout << aux3 << endl;
        }
    }
    return 0;
}

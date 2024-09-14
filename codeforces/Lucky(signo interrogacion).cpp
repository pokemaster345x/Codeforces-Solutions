#include <iostream>
#include <string>
using namespace std;

int main() {
    int t, aux1, aux2;
    string s;
    cin >> t;
    for(int x = 0; x < t; x++) {
        cin >> s;
        aux1 = stoi(s.substr(0, 1)) + stoi(s.substr(1, 1)) + stoi(s.substr(2, 1));
        aux2 = stoi(s.substr(3, 1)) + stoi(s.substr(4, 1)) + stoi(s.substr(5, 1));
        if (aux1 == aux2) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}

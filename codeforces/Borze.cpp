#include <iostream>
#include <string>

using namespace std;

int main() {
    string b;
    cin >> b;

    string t;
    for (size_t i = 0; i < b.length(); ++i) {
        if (b[i] == '.') {
            t += '0';
        } else if (b[i] == '-') {
            if (i + 1 < b.length()) {
                if (b[i + 1] == '.') {
                    t += '1';
                    ++i;
                } else if (b[i + 1] == '-') {
                    t += '2';
                    ++i;
                }
            }
        }
    }

    cout << t << endl;
    return 0;
}

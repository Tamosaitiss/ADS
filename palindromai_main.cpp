#include <iostream>
using namespace std;

bool arPirminis(int skaicius) {
    if (skaicius < 2) return false;
    for (int i = 2; i * i <= skaicius; ++i) {
        if (skaicius % i == 0) return false;
    }
    return true;
}

bool arPalindromas(int skaicius) {
    int original = skaicius, atvirkscias = 0;
    while (skaicius > 0) {
        atvirkscias = atvirkscias * 10 + skaicius % 10;
        skaicius /= 10;
    }
    return original == atvirkscias;
}

int main() {
    char pasirinkimas;
    do {
        int a, b;
        cout << "Iveskite intervalo pradzia (a): ";
        cin >> a;
        cout << "Iveskite intervalo pabaiga (b): ";
        cin >> b;

        bool rasta = false;
        cout << "Palindrominiai pirminiai skaiciai intervale [" << a << ", " << b << "]:" << endl;
        for (int i = a; i <= b; ++i) {
            if (arPirminis(i) && arPalindromas(i)) {
                cout << i << " ";
                rasta = true;
            }
        }

        if (!rasta) {
            cout << "Nerasta palindrominiu pirminiu skaiciu siame intervale.";
        }

        cout << "\nAr norite testi? (t - taip, n - ne): ";
        cin >> pasirinkimas;

    } while (pasirinkimas == 't' || pasirinkimas == 'T');

    cout << "Ciao." << endl;
    return 0;
}
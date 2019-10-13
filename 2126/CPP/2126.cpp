#include <bits/stdc++.h>

using namespace std;
unsigned int qtd_digitos_numero(unsigned int n) {
    unsigned int aux;
    aux = 0;
    while (n >= 1) {
        aux++;
        n /= 10;
    }
    return aux;
}

int main() {
    string numero_1, numero_2;
    size_t qtd_ocorrencias;
    size_t ultimo_caso;
    size_t caso_atual;
    size_t casos;
    casos = 0;
    while (cin >> numero_1) {
        cin >> numero_2;
        qtd_ocorrencias = 0;
        caso_atual = 0;
        while (numero_2.length() >= numero_1.length()) {
            if (equal(numero_1.begin(), numero_1.end(), numero_2.begin())) {
                ultimo_caso = caso_atual + 1;
                caso_atual += numero_1.length();
                qtd_ocorrencias++;
                numero_2.erase(numero_2.find(numero_1), numero_1.length());
            } else {
                numero_2.erase(0, 1);
                caso_atual++;
            }
        }

        cout << "Caso #" << ++casos << ":" << endl;
        if (qtd_ocorrencias > 0) {
            cout << "Qtd.Subsequencias: " << qtd_ocorrencias << endl;
            cout << "Pos: " << ultimo_caso << endl;
        } else {
            cout << "Nao existe subsequencia" << endl;
        }
        cout << endl;
    }
    return 0;
}

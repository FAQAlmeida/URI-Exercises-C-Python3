#include <bits/stdc++.h>

using namespace std;
int max_items(int *sequencia, size_t qtd, size_t index, int sum) {
    if (index == qtd) return sum;
    if (index == 0) {
        return max_items(sequencia, qtd, index + 1, sum + sequencia[index]);
    }
    if (sequencia[index] == 0) {
        return max_items(sequencia, qtd, index + 1, sum);
    }
    return max(max_items(sequencia, qtd, index + 1, sum), max_items(sequencia, qtd, index + 1, sum + sequencia[index]));
}

int min_items(int *sequencia, size_t qtd, size_t index, int sum) {
    if (index == qtd) return sum;
    if (index == 0) {
        return min_items(sequencia, qtd, index + 1, sum + sequencia[index]);
    }
    if (sequencia[index] == 0) {
        return min_items(sequencia, qtd, index + 1, sum);
    }
    return min(min_items(sequencia, qtd, index + 1, sum), min_items(sequencia, qtd, index + 1, sum + sequencia[index]));
}

int main(void) {
    int operacoes[] = {-50, -13500, 200, 550, 13000, -20, 40};
    size_t n;
    char operacao;
    cin >> n;
    int *acoes = new int[n];
    for (size_t i = 0; i < n; i++) {
        cin >> operacao;
        switch (operacao) {
            case 'A': {
                acoes[i] = operacoes[0];
                break;
            }
            case 'C': {
                acoes[i] = operacoes[1];
                break;
            }
            case 'S': {
                acoes[i] = operacoes[2];
                break;
            }
            case 'P': {
                acoes[i] = operacoes[3];
                break;
            }
            case 'M': {
                acoes[i] = operacoes[4];
                break;
            }
            case 'K': {
                acoes[i] = operacoes[5];
                break;
            }
            case 'B': {
                acoes[i] = operacoes[6];
                break;
            }
            case 'N': {
                acoes[i] = 0;
                break;
            }
            default:
                break;
        }
    }
    cout << max_items(acoes, n, 0, 0) << " " << min_items(acoes, n, 0, 0);
    return 0;
}

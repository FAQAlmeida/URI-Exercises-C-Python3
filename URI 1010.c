#include <stdio.h>
 
int main() {
 
    int Cod1, Cod2, Quant1, Quant2;
	double Valor1, Valor2, Pagar;

	scanf("%d %d %lf", &Cod1, &Quant1, &Valor1);
	scanf("%d %d %lf", &Cod2, &Quant2, &Valor2);
	Pagar = (Quant1 * Valor1) + (Quant2 * Valor2);
	printf("VALOR A PAGAR: R$ %.2lf\n", Pagar);
 
    return 0;
}
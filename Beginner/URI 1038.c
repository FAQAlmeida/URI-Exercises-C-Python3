#include <stdio.h>
 
int main() {

    int cod,quant;
	double price,Valor;

	scanf("%d %d", &cod, &quant);
	
	if (cod == 1)
	{
		price = 4;
	}
	if (cod == 2)
	{
		price = 4.5;
	}
	if (cod == 3)
	{
		price = 5;
	}
	if (cod == 4)
	{
		price = 2;
	}
	if (cod == 5)
	{
		price = 1.5;
	}

	Valor = price * quant;

	printf("Total: R$ %.2lf\n", Valor);
 
    return 0;
}
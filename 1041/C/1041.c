#include <stdio.h>
 
int main() {
 
    double a, b;

	scanf("%lf", &a);
	scanf("%lf", &b);

	if (a == 0.0 && b == 0.0)
	{
		printf("Origem\n");
	}
	else if (b == 0.0 && a != 0.0)
	{
		printf("Eixo X\n");
	}
	else if (a == 0.0 && b != 0.0)
	{
		printf("Eixo Y\n");
	}
	else if (a > 0.0 && b > 0.0)
	{
		printf("Q1\n");
	}
	else if (a < 0.0 && b > 0.0)
	{
		printf("Q2\n");
	}
	else if (a < 0.0 && b < 0.0)
	{
		printf("Q3\n");
	}
	else if (a > 0.0 && b < 0.0)
	{
		printf("Q4\n");
	}
 
    return 0;
}
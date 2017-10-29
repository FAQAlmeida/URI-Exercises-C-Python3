#include <stdio.h>
 
int main() {
 
    double sal, a, b, c;

	scanf("%lf", &sal);

	if (sal <= 2000)
	{
		printf("Isento\n");
	}
	else if (sal > 2000 && sal <= 3000)
	{
		a = sal - 2000;
		a = a * 8 / 100;
		printf("R$ %.2lf\n", a);
	}
	else if (sal > 3000 && sal <= 4500)
	{
		a = 1000;
		b = sal - 3000;
		a = a * 8 / 100;
		b = b * 18 / 100;
		a += b;

		printf("R$ %.2lf\n", a);
	}
	else
	{
		b = 1500;
		a = 1000;
		c = sal - 4500;
		a = a * 8 / 100;
		b = b * 18 / 100;
		c = c * 28 / 100;
		
		a += b + c;

		printf("R$ %.2lf\n", a);
	}
 
    return 0;
}
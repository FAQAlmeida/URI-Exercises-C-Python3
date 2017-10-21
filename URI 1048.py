#include <stdio.h>
 
int main() {
 
    double a, b;
	int c;
	scanf("%lf", &a);

	if (a <= 400.00) { b = a * 15 / 100; a += b; c = 15;}
	else if(a<=800.00){ b = a * 12 / 100; a += b; c = 12; }
	else if (a<=1200.00) { b = a * 10 / 100; a += b; c = 10; }
	else if (a <= 2000.00) { b = a * 7 / 100; a += b; c = 7; }
	else{ b = a * 4 / 100; a += b; c = 4; }

	printf("Novo salario: %.2lf\n", a);
	printf("Reajuste ganho: %.2lf\n", b);
	printf("Em percentual: %d %\n", c);
 
    return 0;
}
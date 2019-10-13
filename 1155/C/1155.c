#include <stdio.h>
 
int main() {
 
    double S = 0;
	double a;

	for (a = 1; a <= 100; a++)
	{
		S = S + 1 / a;
	}

	printf("%.2lf\n", S);
 
    return 0;
}
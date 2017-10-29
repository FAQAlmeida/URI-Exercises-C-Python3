#include <stdio.h>
 
int main() {
 
    double A, B, C, delta;

	scanf("%lf %lf %lf", &A, &B, &C);

	if (A == 0)
	{
		printf("Impossivel calcular\n");
	}
	else
	{
		delta = (pow(B, 2)) - (4 * A * C);

		if (delta < 0)
		{
			printf("Impossivel calcular\n");
		}
		else
		{
			double X1, X2;

			X1 = (-B + sqrt(delta)) / (2 * A);
			X2 = (-B - sqrt(delta)) / (2 * A);

			printf("R1 = %.5lf\nR2 = %.5lf\n", X1, X2);

		}
	}
 
    return 0;
}
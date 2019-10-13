#include <stdio.h>
 
int main() {
 
    double raio, A, PI = 3.14159;

	scanf("%lf", &raio);
	A = (raio*raio)*PI;
	printf("A=%0.4lf\n", A);
 
    return 0;
}
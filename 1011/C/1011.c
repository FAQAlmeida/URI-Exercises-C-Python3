#include <stdio.h>
 
int main() {
 
    double raio,pi = 3.14159, Resul;

	scanf("%lf", &raio);
	Resul = (4.0 / 3) * pi * (raio*raio*raio);
	printf("VOLUME = %0.3lf\n", Resul);
 
    return 0;
}
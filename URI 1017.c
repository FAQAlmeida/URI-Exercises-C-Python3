include <stdio.h>
 
int main() {
 
    double KM,Temp,gasto;

	scanf("%lf %lf", &KM, &Temp);
	gasto = (KM * Temp) / 12;
	printf("%0.3lf\n", gasto);
 
    return 0;
}
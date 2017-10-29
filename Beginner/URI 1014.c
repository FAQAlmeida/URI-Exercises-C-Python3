#include <stdio.h>
 
int main() {
 
    int X;
	double Y,Cons;
	scanf("%d %lf", &X, &Y);
	Cons = (X / Y);
	printf("%0.3lf km/l\n", Cons);
 
    return 0;
}
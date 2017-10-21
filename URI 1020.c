#include <stdio.h>
 
int main() {
 
    int Y = 0,M = 0,D = 0,I;
	scanf("%d", &I);

	Y = I / 365;
	I = I % 365;
	M = I / 30;
	D = I % 30;

	printf("%d ano(s)\n", Y);
	printf("%d mes(es)\n", M);
	printf("%d dia(s)\n", D);
}
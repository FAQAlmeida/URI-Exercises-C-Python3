#include <stdio.h>
 
int main() {
 
    int a[3] = { 3600,60,1 };
	int b[3], i, N;
	scanf("%d", &N);
	for (i = 0; i<3; i++) 
	{
		b[i] = N / a[i];
		N = N%a[i];
	}
	printf("%d:%d:%d\n", b[0], b[1], b[2]);
 
    return 0;
}
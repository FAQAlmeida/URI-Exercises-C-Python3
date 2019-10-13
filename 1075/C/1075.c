#include <stdio.h>
 
int main() {
 
    int N, a, b;

	scanf("%d", &N);

	for (a = 1; a <= 10000; a++)
	{
		b = a % N;

		if (b == 2)
		{
			printf("%d\n", a);
		}
	}
 
    return 0;
}
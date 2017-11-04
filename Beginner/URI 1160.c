#include <stdio.h>
 
int main() {
 
    int N,f,x,a;
	int CI1, CI2;
	double C1, C2;

	scanf("%d", &N);

	for(f=1;f<=N;f++)
	{
		scanf("%d %d %lf %lf", &CI1, &CI2, &C1, &C2);
		x = 0;

		while (CI1 <= CI2)
		{
			
			CI1 *= (C1 / 100.0) + 1;
			CI2 *= (C2 / 100.0) + 1;
			x++;

			if (x > 100)
			{
				printf("Mais de 1 seculo.\n");
				break;
			}
		}
		if (x <= 100)
		{
			printf("%d anos.\n", x);
		}
	}
 
    return 0;
}
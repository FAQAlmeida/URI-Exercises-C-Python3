#include <stdio.h>
 
int main() {
 
    int i;
	double n[4], media = 0;

	for (i = 0; i < 4; i++)
	{
		scanf("%lf", &n[i]);
	}

	n[0] = n[0]*2/10;
	n[1] = n[1]*3/10;
	n[2] = n[2]*4/10;
	n[3] = n[3]*1/10;

	for (i = 0; i < 4; i++)
	{
		media += n[i];
	}

	printf("Media: %.1lf\n", media);

	if (media >= 5 && media <= 6.9)
	{
		double ne;

		printf("Aluno em exame.\n");
		scanf("%lf", &ne);

		printf("Nota do exame: %.1lf\n", ne);

		ne = (ne + media) / 2;

		if (ne >= 5)
		{
			printf("Aluno aprovado.\n");
		}
		else
		{
			printf("Aluno reprovado.\n");
		}
		printf("Media final: %.1lf\n", ne);
	}
	else if (media < 5)
	{
		printf("Aluno reprovado.\n");
	}
	else
	{
		printf("Aluno aprovado.\n");
	}
 
    return 0;
}
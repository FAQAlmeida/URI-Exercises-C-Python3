#include <stdio.h>
 
int main() {
 
    int Name[30];
	double SalaryFix,Quant,Total;

	scanf("%s", &Name);
	scanf("%lf %lf", &SalaryFix,&Quant);
	Total = SalaryFix +( Quant * 15/100);
	printf("TOTAL = R$ %0.2lf\n",Total);
 
    return 0;
}
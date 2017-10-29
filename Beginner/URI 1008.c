#include <stdio.h>
 
int main() {
 
    int Number,Hour;
	double Salary,Price;

	scanf("%d %d", &Number, &Hour);
	scanf("%lf", &Price);
	Salary = (Price * Hour);
	printf("NUMBER = %d\n",Number);
	printf("SALARY = U$ %0.2lf\n",Salary);
 
    return 0;
}
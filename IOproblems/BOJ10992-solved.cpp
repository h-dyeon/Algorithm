#include <iostream>
using namespace std;
int main() {
	int x;
	scanf_s("%d", &x);

	for (int i = 0;i < x-1;i++) {
		for (int j = 0;j < x - 1-i;j++)printf(" ");
		for (int j = 0;j < 2 * i+1 ;j++) {
			if(j==0)printf("*");
			if(j == 2 * i-1)printf("*");
			else printf(" ");
		}
		printf("\n");
	}
	for (int j = 0;j < 2*x-1;j++)printf("*");
}
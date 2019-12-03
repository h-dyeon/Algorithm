#include <iostream>
using namespace std;
int main() {
	int x;
	scanf_s("%d", &x);

	for (int i = 0;i < x;i++) {
		for (int j = 0;j < i+1;j++) {
			printf("*");
		}
		printf("\n");
	}
}